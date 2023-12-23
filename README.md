# BUG TRACKER API

Bugtracker API is a suite for managing bugs.

This API help teams work better by enabling every member on a team to submit and correct bugs. This app is geared towards developers, QA testers, project managers and product owners.

## Features

The following are the features of this application

1. User Authentication and Authorization
2. Bug Reporting
3. Bug listing and Sorting
4. Bug assignment and tracking
5. Bug visualization
6. Testing and quality assurance

## Tech Stack

- FastAPI
- MongoDB

## Set up

The first thing is to ensure you have [poetry](https://python-poetry.org) installed. With that said, you have to make sure you have access to a MongoDB server. Docker is welcomed! and make sure it is open on port 27017. Next...

1. `git clone https://github.com/ademolab91/bugtacker-v3`
2. `cd bugtracker-v3/backend`
3. `poetry install`
4. `uvicorn backend.main:app`

Goto [https://localhost:8000/docs](https://localhost:8000/docs)

### Use the API

- Register a new user

  ![bugtracker-image-1](/assets/bt_1.png)

- Login

  ![bugtracker-image-2](/assets/bt_2.png)

- Create a project

  ![bugtracker-image-3](/assets/bt_3.png)

- Report a bug

  ![bugtracker-image-4](/assets/bt_4.png)
  
  ...

## Documentation

This API has been properly documented with Postman. Go through it [here](https://blue-equinox-253771.postman.co/workspace/Bugtracker-Workspace~53330d62-ce7e-4113-b3f6-caccec3be939/collection/25671522-57599221-f8b7-4729-bd10-5faf4e6f470c?action=share&creator=25671522)

## Kudos

Special big shoutout to the creators of [fastapi-users](https://fastapi-users.github.io/) and [beanie odm](https://beanie-odm.dev/). These tools sped up my development process a ton.

## Outro

I am Ademola Balogun
I can be reached via email at: [ademolabalogun91@gmail.com](https://mailto:ademolabalogun91@gmail.com)
