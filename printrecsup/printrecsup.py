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

# In[7]:


import pymongo
import arrow


# In[8]:


import boto3


# In[9]:


s3 = boto3.resource('s3')


# In[ ]:





# In[10]:


#s3.create_bucket(Bucket='printrecsup')
#s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
#    'LocationConstraint': 'us-west-1'})


# In[11]:


#for bucket in s3.buckets.all():
#    print(bucket.name)


# In[12]:


#data = open('/home/pi/Downloads/87-philghcq.png', 'rb')
#s3.Bucket('printrecsup').put_object(Key='87-philghcq.png', Body=data)


# In[59]:




clirek = boto3.client('rekognition')


# In[60]:


#https://printrecsup.s3.amazonaws.com/87-philghcq.png


# In[61]:


client = boto3.client('translate')


# In[39]:


#response = client.translate_text(
#    Text='hello there.',
    
#    SourceLanguageCode='auto',
#    TargetLanguageCode='zh'
#)


# In[14]:


with open('/home/pi/mongo.txt', 'r') as monconf:
    monc = monconf.read().replace('\n', '')


# In[15]:



client = pymongo.MongoClient(monc)


# In[16]:


db = client['printrecsup']

# Fetch our series collection
series_collection = db['print']


# In[17]:


#post = {"image" : "pi.png", "id" : uuid.uuid4(), "username" : 'william', 'datetime': datetime.timestamp,
#       'datedue' : duedate.timestamp}


# In[82]:


def createentry(imagepath, filename, username, price, quantity, duehours, printcompany, status):
    response = client.translate_text(
    Text=status,
    SourceLanguageCode='auto',
    TargetLanguageCode='zh')
    

    datetime = arrow.now()
    duedate = datetime.shift(hours=duehours)
    data = open(imagepath + filename, 'rb')
    s3.Bucket('printrecsup').put_object(Key=filename, Body=data)
    
    resp = clirek.detect_labels(
    Image={
        
        'S3Object': {
            'Bucket': 'printrecsup',
            'Name': filename
        }})

    somelis = list()
    for reslab in resp['Labels']:
        #print(reslab['Name'])
        somelis.append(reslab['Name'])
    
    post = {'image' : 'https://printrecsup.s3.amazonaws.com/' + filename, 
            'username' : username, 'price' : price, 'quantity' : quantity,
            'totalinvoice' : price * quantity, 'datetime': datetime.timestamp, 'datedue' : duedate.timestamp,
    'printer' : printcompany, 'status' : status, 'zhstatus' : response['TranslatedText'],
           'labels' : somelis}
    return(series_collection.insert_one(post).inserted_id)

    #return(inserted_id)
    


# In[ ]:





# In[83]:


def find_document(elements, multiple=False):

    return series_collection.find_one(elements)


# In[84]:


#createentry('/home/pi/Downloads/', '87-philghcq.png', 'william', 
#            
#            500, 50, 12, 
#            'zoomprint', 'created')


# In[85]:


find_document({'image' : 'https://printrecsup.s3.amazonaws.com/87-philghcq.png'})


# In[26]:


#createentry('/home/pi/Downloads/', 'Gates.png', 'william', 500, 12, 'zoomprint', 'finished')


# In[45]:


#createentry('/home/pi/Downloads/', 'download.jpeg', 'william', 500, 12, 'zoomprint', 'created')


# In[ ]:





# In[27]:


def find_document(elements, multiple=False):

    return series_collection.find_one(elements)


# In[ ]:





# In[30]:


#find_document({'username' : 'william'})


# In[ ]:





# In[ ]:


def find_document(elements, multiple=False):

    return series_collection.find_one(elements)

