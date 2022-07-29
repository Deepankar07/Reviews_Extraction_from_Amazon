import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

link='https://www.amazon.in/Backpack-Small-Black-Water-Repellant/product-reviews/B088XB5XY8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page=requests.get(link)

#Parsing of html
soup=bs(page.content,'html.parser')


#Next step we require name of user (Its difficult to find a particular username in the complex data)
#Go to review page click on that name and inspect page
#After that copy the class name form it and also write name of the tag eg. "span"

names=soup.find_all('span',class_='a-profile-name')


#To store only the names not all irrelevant info
#Creating list
cust_name=[]
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
#print(cust_name)    

#Some names are repeating so removing it---
cust_name.pop(0)
cust_name.pop(0)
cust_name.pop(0)
cust_name.pop(4)
cust_name.pop(7)
cust_name.pop(4)
cust_name.pop(6)
#print(cust_name)    


#Extracting Review_Title
titles=soup.find_all('a',class_='review-title-content')
review_title=[]
for i in range(0,len(titles)):
    review_title.append(titles[i].get_text())
#print(review_title)  ---->  #We get '/n' with the title to remove it code below
review_title[:] = [titles.strip('\n') for titles in review_title]
#print(review_title) 


#Extracting Ratings
ratings=soup.find_all('i',class_='review-rating')
rating=[]
for i in range(0,len(ratings)):
    rating.append(ratings[i].get_text())
rating.pop(0)
rating.pop(0)
#print(rating)    


#Extracting Review content
reviews=soup.find_all('span',class_='review-text-content')
#OR--->
#reviews=soup.find_all("span",{"data-hook":"review-body"})
review_content=[]
for i in range(0,len(reviews)):
    review_content.append(reviews[i].get_text())
review_content[:]=[reviews.strip("\n") for reviews in review_content]
#print(review_content) 

df=pd.DataFrame()
df["Customer Name"]=cust_name
df["Title Review"]=review_title
df["Rating"]=rating
df["Reviews"]=review_content
print(df)
df.to_csv("AmazonReviews3.csv")

