#!/usr/bin/env python
# coding: utf-8

# 3d printer image recognition and supply 
# 
# create a ticket. photo of part. id, username, 
# datetime created, datetime due, price, status, print company. 
# 
# get a ticket.
# 
# assign a ticket.
# 
# choose to assign ticket to someone. 
# 
# delete a ticket. 
# 
# 
# 

# In[1]:


import pymongo
import arrow


# In[2]:


import boto3


# In[3]:


s3 = boto3.resource('s3')


# In[ ]:





# In[4]:


#s3.create_bucket(Bucket='printrecsup')
#s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
#    'LocationConstraint': 'us-west-1'})


# In[6]:


#for bucket in s3.buckets.all():
#    print(bucket.name)


# In[158]:


#data = open('/home/pi/Downloads/87-philghcq.png', 'rb')
#s3.Bucket('printrecsup').put_object(Key='87-philghcq.png', Body=data)


# In[ ]:





# In[ ]:


#https://printrecsup.s3.amazonaws.com/87-philghcq.png


# In[129]:


with open('/home/pi/mongo.txt', 'r') as monconf:
    monc = monconf.read().replace('\n', '')


# In[130]:



client = pymongo.MongoClient(monc)


# In[131]:


db = client['printrecsup']

# Fetch our series collection
series_collection = db['print']


# In[132]:


#post = {"image" : "pi.png", "id" : uuid.uuid4(), "username" : 'william', 'datetime': datetime.timestamp,
#       'datedue' : duedate.timestamp}


# In[163]:


def createentry(imagepath, filename, username, price, duehours, printcompany, status):
    datetime = arrow.now()
    duedate = datetime.shift(hours=duehours)
    data = open(imagepath + filename, 'rb')
    s3.Bucket('printrecsup').put_object(Key=filename, Body=data)
    post = {"image" : 'https://printrecsup.s3.amazonaws.com/' + filename, "username" : username, 
     'datetime': datetime.timestamp, 'datedue' : duedate.timestamp,
    'printer' : printcompany, 'status' : status}
    return(series_collection.insert_one(post).inserted_id)

    #return(inserted_id)
    


# In[164]:


#createentry('/home/pi/Downloads/', 'blackyome.png', 'william', 500, 12, 'zoomprint', 'created')


# In[135]:


def find_document(elements, multiple=True):

    return series_collection.find_one(elements)


# In[136]:


#find_document({'image' : '/home/pi/pi.png'})

