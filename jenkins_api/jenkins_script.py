import requests
import jenkins
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Jenkins_Api_Actions():

	def CreateDb():
		engine = create_engine('sqlite:///cli.db', echo=False)
		session = sessionmaker(bind=engine)()
		Base.metadata.create_all(engine)
		return session
		
	def connectToJenkins(url, username, password):
		server = jenkins.Jenkins(url, 
		username=username, password=password)
		return server

	def addJob(session, jlist):
		for j in jlist:
			session.add(j)
		session.commit()

	def getLastJobId(session, name):
		job = session.query(Jobs).filter_by(name=name).order_by(Jobs.jen_id.desc()).first()
		if (job != None):
			return job.jen_id
		else:
			return None
			
class Jenkins_Jobs_Details(Base):
    __tablename__ = 'Jobs'

    id = Column(Integer, primary_key = True)
    jen_id = Column(Integer)
    name = Column(String)
    timeStamp = Column(DateTime)
    result = Column(String)
    building = Column(String)
    estimatedDuration = Column(String)

def createJobList(start, lastBuildNumber, jobName, server):
    jobs_List = []
    for i in range(start + 1, lastBuildNumber + 1):
        current = server.get_build_info(jobName, i)
        current_as_jobs = Jenkins_Jobs_Details()
        current_as_jobs.jen_id = current['id']
        current_as_jobs.building = current['building']
        current_as_jobs.estimatedDuration = current['estimatedDuration']
        current_as_jobs.name = jobName
        current_as_jobs.result = current['result']
        current_as_jobs.timeStamp = datetime.datetime.fromtimestamp(long(current['timestamp'])*0.001)
        jobs_List.append(current_as_jobs)
    return(jobs_List)

def connect_and_store(url,username,password):	
	jenkins = Jenkins_Api_Actions()
	server = jenkins.connectToJenkins(url, username, password)
	authenticated = false
	try:
		server.get_whoami()
		authenticated = true
	except jenkins.JenkinsException as e:
		print('Authentication error')
		authenticated = false

	if authenticated:
		session = jenkins.CreateDb()

		# get a list of all jobs
		jobs = server.get_all_jobs()
		for j in jobs:
			jobName = j['name'] # get job name
			#print jobName
			lastJobId = jenkins.getLastJobId(session, jobName) # get last locally stored job of this name
			lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']  # get last build number from Jenkins for this job 
			
			# if job not stored, update the db with all entries
			if lastJobId == None:
				start = 0
			# if job exists, update the db with new entrie
			else:
				start = lastJobId

			# create a list of unadded job objects
			jobs_list = createJobList(start, lastBuildNumber, jobName, server)
			# add job to db
			jenkins.addJob(session, jobs_list)

if __name__ = '__main__':
	url = 'http://localhost:8080'
	username = raw_input('Enter username: ')
	password = raw_input('Enter password: ')
	connect_and_store(url,username,password)