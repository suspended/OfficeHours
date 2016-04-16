# Office Hours

## Inspiration
The short - Have you ever been faced with a problem set that spanned the contents of five chapters of an unfamiliar textbook? Flipping through the pages, looking up at the clock, then looking back down again, searching for that one keyword where the answer could be found?

Our team wanted to brainstorm an idea  to use the Watson Developer Cloud APIs in a meaningful way that solves a problem people face. One of the ideas we had was to use Natural Language Classifier and Retrieve and Rank to interpret privacy policies of websites and compare their relative privacy (in)-adequacies through their legalese. This could be a possible idea for a future project. However, since we were in college, our final idea revolved around making learning easier - and this was how Office Hours was born.

## What it does
The short - Office Hours is a web app where you can upload your text, ask related questions and our app will give you a summary of the answers that lay in your text.

The instructor or student can upload a set of documents to search on. The instructor can then define a ground truth CSV file for that specific class or topic, or use the default ground truth file, which might not work as well, for non-STEM classes. The backend will rerank the dataset as necessary, every few hours. 

## How I built it
The uploaded files are passed through to the Document Conversion API into Answer Units JSON, which is then further parsed and cleaned, before feeding it into the Solr cluster via the Retrieve and Rank API. Our backend was built in Flask and Python.

## Challenges we ran into
- This is the first time that either of us have tried anything remotely related to machine learning. We had some difficulty training the Retrieve and Rank API to generate data that was relevant to the questions asked.
- Grasping the nuances of the Solr cluster and configuration was tough. 
- Also, we wanted to do away with the ground truth file and automatically generate the file by using the other Watson APIs like the Concept Expansion and Insights APIs. However, we realized that the sentence structure of the questions are also parsed and simply feeding it concepts will not cut it if we want to allow complex sentences to be searched.

## What's next for Office Hours
- Improving the UI
- Monitoring a folder for changes and syncing it to the Solr cluster without any need for manual uploading
- Allow each user to have their own custom search engine - think your own personal document search engine
- We want to allow users to create accounts so that they do not have to upload their documents each time they visit the site.
- Nicer representation of search results

## Demo
The original data set was culled from the Cranfield collection - http://ir.dcs.gla.ac.uk/resources/test_collections/cran/ So question pertaining to that will be most accurate. We did add a variety of random datasets after that - and you can try it out.
