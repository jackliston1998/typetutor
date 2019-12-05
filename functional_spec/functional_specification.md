# Functional Specification For Touch Typing Tutorial
__Student 1:__ Shane Grouse
__Student Number:__ 17502633


__Student 2:__ Jack Liston 
__Student Number:__ 17497764

---
__Supervisor:__ Dr. Thomas Ward 
__Completion Date:__ 06/12/2018


## Table of Contents
1. **Introduction**
    1.1 Overview
    1.2 Business Context
    1.3 Glossary
2. **General Description**
    2.1 Product / System Function
    2.2 User Characteristics and Objectives
    2.3 Operational Scenarios
    2.4 Constraints
3. **Functional Requirements**
    3.1 Web cam integration
    3.2 Keyboard detection
    3.3 Text Prompt Generation
    3.4 Keystroke recognition
    3.5 Finger Position Recognition
    3.6 Result feedback
    3.7 Accounts and Data
    3.8 Web app integration
4. **System Architecture**
5. **High-Level Design Diagrams**
6. **Preliminary Schedule**
    6.1 Gantt Charts 


## 1. Introduction

### 1.1 Overview
Our Touch-Typing Tutor system is an interactive learning environment for teaching users how to efficiently touch-type, thus increasing the speed of their typing and increasing their workflow. It replicates most typing tutorials such as Mavis Beacon, however, it will include input from a webcam that is fixed on the keyboard to ensure that the user is using the optimal finger in accordance with the touch-typing methodology. This system will be built using python and we will be integrating our project will OpenCV to allow us to build a map of co-ordinates for the keys on the keyboard as well as tracking the user's fingers. We also hope to integrate with Flask which is a web framework used to create python web apps.

Touch typing is the most effective and efficient way of typing on a keyboard. Surprisingly, it is an uncommon skill that not many people have. There are also few to no opportunities to learn it. The majority of people rely on "hunt and peck" typing (typing by looking at the keyboard) rather than learning to touch type. This trend will likely continue as touch screen devices become more dominant, especially with younger generations. We hope that our project will be able to help teach touch typing to anyone and everyone, regardless of if you are a beginner or you in need of fixing your bad habits.

This system has 4 main functions, reading user input from a keyboard, taking input via webcam on the position of your fingers at the moment of a keystroke, showing the user a prompt that will target the user's most frequently mistyped words and a database that will store the user's typing data as well as their login credentials. 
### 1.2 Business Contect
This project has no relavent business contracts
### 1.3 Glossary
- Touch Typing
    - This is a method of typing in which your index fingers are archored to the f and j keys respectively. You then align each of you remaining fingers to the keys that lead to the edge of the keyboard. Each finger is then assigned a number of keys that only it is allow to hit. See Appendix 7.1 for a visual diagram of how the keys are assigned to each finger.
- Words per minute (WPM)
    - Words per minute is the most common measure of somebodies typing speed. You simply take the number of words written by the user and divide it my the time(in minutes) that you have allocated for them to type.
- Keystroke
    - This is the act of hitting a key on a keyboard to input the information you wish to pass to your device.
- Framerate
    - A video is comprised of a certain amount of static images that display per second. The amount of images shown in a given timeframe is referred to as the framerate of that video. Framerate is most common messured per second and most modern camera will record in the area of 60 frame per second, meaning that camera framrate would be 60 frames oer second.
- OpenCV
    - OpenCV is a library of programming functions mainly aimed at real-time computer vision.
- Flask
    - Flask is a micro web framework written in Python. It is used to create applications in python that can be integrated into websites.
- Python
    - Python is an interpreted, high-level, general-purpose programming language.
- Nginx
    - Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. 
- MongoDB
    - MongoDB is an open source database management system (DBMS) that uses a document-oriented database model which supports various forms of data. Instead of using tables and rows as in relational databases, the MongoDB architecture is made up of collections and documents.



## 2. General Description
### 2.1 Product / System Function
#### *Taking user input.*
For this project, we will be collecting three types of input from the user, visual input on the location of the user's finger at each keystroke(via a webcam using the "OpenCV" library), a record of each user keystroke and the time taken to complete the task allocated to the user.

The recorded keystroke and the location of the desired finger to make that keystroke are imperative to allow us to know whether the user is successfully touch typing and the time will allow us to generate their typing speed in words per minute.

#### *Analysis of user input*
Once we have successfully acquired the user's input we must analyze the user data and output our desired feedback. First, we must check which key has been pressed and if it is the required key according to the prompt on the screen. Then using OpenCV we will find the finger that pressed the key and compared it to see if it is the optimal finger according to the traditional touch-typing method. Once we have gathered the information on if the correct key is pressed and if the correct finger was used we will update our chosen memory structure with this information. Once the memory structure has been updated we repeat the process until the task has been completed by the user.
 
#### *Displaying the analysed user data*
This functionality will be responsible for giving the users feedback on their typing performance. We plan to do so via two main methods, firstly being simply displaying some of the raw data to the user with no visual enhancements, for example, simply printing their words per minute, the percentage of successful keystrokes and the percentage of keystrokes with the correct finger. Secondly, we would like to implement more visually stimulating forms of feedback like a heatmap of the keyboard illustrating areas that have a particularly high concentration of errors. Additionally, this data will be used to create the users' next test prompt to ensure they are getting an effective and, engaging tutorial.

#### *User data storage and accounts*
If the user has not signed up for the site then they will be required to create an account. Once we have taken the user's desired username and password we will store them alongside the user's unique ID. Once the user completes their first typing task their results will be stored in a dictionary. The next game will read from this dictionary and create a prompt using words that mainly contain the letters which they used incorrectly. Once the user signs out we plan on storing their current progress in our MongoDB as an alpha-numeric string we will create via a simple parser that will run through the dictionary. When the user signs in again to use the tutorial we will pull the alpha-numeric string through our parser and insert it into our dictionary. The use of this dictionary also us to standardize how our user's data is represented and represent it in the easiest way possible.

### 2.2 User Characteristics and Objectives
In terms of user expertise, there is not a lot required. Users should be some what familiar with computing and have a basic understanding of computers e.g how to operate one, how to open an application. Our ideal goal would be to host our project as a web interface. This would make it very easy for users to access our system and would not require any downloads/installs. It is preferred that users have knowledge of the standard letter layout on a keyboard. This is not necessary as it can be learned while interacting with the application. Being familiar with the keyboard layout is a key part of touch typing and it is beneficial if users already have this experience.

There are however some system requirements. The first requirement is a computer with a monitor and functional keyboard. The program will not be compatible with touch screens and a physical keyboard is needed to monitored a users finger positions for each keystroke. Another hardware requirement is a camera or web cam that can focus on your keyboard. Laptops with built in cameras can't unfortunately be used as the camera angle cannot capture the keyboard (a mirror attachment on top of laptop may work). Good lighting is also needed to allow the camera to correctly record the keyboard.

The main objective for our users is to learn how to correctly touch type in an effective way. This will be achieved by the system checking that the user is correctly touch typing, allowing the user to focus on typing and learning. Our program will supply users with typing lessons, display their results and highlight mistakes that were made. Typing speed, key proficiency and finger accuracy are the different areas that we want users to improve upon. Feedback will be given back with these areas in mind, especially finger accuracy. Regardless of if you are only starting to type or you need a refresher session, these key objectives apply to users of all levels.


### 2.3 Operational Scenarios
The first step is to acquire and set up a suitable recording device (camera/web cam). Plug this camera into the desktop and set it to aim at the keyboard. The camera or its setup should not infringe on the users view of their monitor. Next, the user will start the program or sign in on the web app. Instructions will then appear on screen on how to focus the camera on the keyboard. Follow these instructions until the camera correctly identifies the keyboard. The user is know ready to begin.

Users can then begin their first typing tutorial. This consists of typing a set amount of words that are displayed on the screen. Users attempt to type these words using touch typing. Meanwhile, the camera monitors which finger was used for each keystroke and checks if the correct finger (according to touch typing standards) is used. When all the words have been typed, results are given back to the users. Accuracy, speed and mistakes will be displayed to users. The users next tutorial will then have words generated based on the mistakes from their last tutorial/their most common mistakes. Their data on most common mistakes will be stored and linked to their account, so it is accessible when they log in next.


### 2.4 Constraints
The biggest constraint is the camera/web cam. While we can use our laptop cameras for testing OpenCV, lighting and quality, we need a device that can focus on the keyboard for the majority of the development. This means we have to research, choose and obtain a camera as soon as possible. Frame rate is the most important spec of the camera as it serves as one of our hardware limitations. There is a possibility that the user types faster then the cameras frame rate, meaning the camera will not be able to register every keystroke. This should only occur with very fast typers or particularly slow frame rates. Hopefully our first choice camera will be sufficent for the majority of people. If not, we will need to get another. Lastly, we will need to get ethical approval for testing on independent users as our project involves recording/picturing users.



## 3. Functional Requirements
### *3.1 Web cam integration*
**Description**
The first and most critical aspect of this project is our integration with OpenCV. Numerous websites already exist that can take user input from a keyboard and return a user's words per minute as well as their accuracy in making the correct keystroke. However, we are pursuing something that, from our research does not publicly exist. Taking user input from the camera allows us to take more user data and thus produce a far superior tool to increase a typist's proficiency.
**Criticality**
The first and most critical aspect of this project is our integration with OpenCV.
**Technical issues**
So long as a user as an active internet connects and a webcam that can be pointed at the keyboard we will be able to record the location of their fingers
**Dependencies with other requirements**
This is not dependant on any other requirements 

### *3.2 Keyboard detection* 
**Description**
In the first functionality, we merely integrated with OpenCV and gave it the ability to see. This functionality will comprise of two main objections well as one dependency. Firstly this functionality aims to recognize a keyboard and create a border around exclusively the alphabetical keys. Secondly, it aims to assign co-ordinates to the keys on the registered keyboard.
**Criticality**
It is critical highly critical to the finger positional recognition as it will map the area and position of each key and provide it with co-ordinates that will be saved and referred to as our user takes our touch typing tutorial.
**Technical issues**
Variations in lighting could lead to some issues with applying the co-ordinates to the 
**Dependencies with other requirements**
This functionality will depend on the first functionality mentioned as it must have the ability to "see" the keyboard by using OpenCV. 

### *3.3 Text Prompt Generation*
**Description**
For our user's to use our tutor they will have to take a typing test in which a series of words will appear in front of them on screen. This functionality will generate and display this prompt to the user. If it is the user's first time using the application will present them with a test prompt that will require ever key to be pressed at least once. From this, a data set on the user will be created. It is then the job of the prompt to output the typing test that would most challenge the user.
**Criticality**
This functionality is fully critical to this project as if it were to fail then the user would have no prompt to be tested on.
**Technical issues**
To simplify this functionality we will have premade typing tutorials that we will simply refer to according to what we believe will best suit the user. Implementing the ability to create unique sentences would be a great addition to our project but we believe it to be an unnecessary complication as the project stands.
**Dependencies with other requirements**
To create the prompts it will be reliant on result feedback so that targetted prompts are  chosen and generated

### *3.4 Keystroke recognition*
**Description**
This functionality will be responsible for recognizing each of the user's keystrokes. It will read from the prompt and it will compare each keystroke input by the user with the expected key given by the prompt. If the keystrokes are not a match then this input will be deemed incorrect and this data will be passed to the user's dataset.
**Criticality**
If the keystrokes match then this will be passed to the Finger positional recognition functionality to ensure that the keypress is a success. This makes it critical to our project as we must ensure that the correct keys are being inputted
**Technical issues**
Being able to compute if it is the correct keystroke quickly enough for the project to be usable
**Dependencies with other requirements**
This functionality relies on the Text Prompt Generator as the user needs a prompt to type and functionality needs to compare the keystrokes to see if they are in fact correct.

### *3.5 Finger Position Recognition*
**Description**
This functionality will track the position of each of your fingers as it looks at the keyboard. Once the keystroke has been made the expected coordinates of that keys position will be given and now this functionality will assert which finger is at that position at the moment the key was pressed. It will then check if that key is correct to return the results to the database
**Criticality**
This positional finger recognition is the final step required to hit our inner scope for this project so it is critical to the project as it is essentially the entire thing that distinguishes the project.
**Technical issues**
Fingers leaving and entering the frame and calculating all of the answers in real-time may lead us to run into some technical issue
**Dependencies with other requirements**
This is dependant of the webcam integration and keyboard detection.

### *3.6 Result feedback*
**Description**
This functionality is responsible for giving the user targetted test prompts for their typing tests. It will read the data that has been stored after the user's past typing tests have been completed and it will output a prompt for the user's next test that is targetted at their most common mistakes.
**Criticality**
This functionality is not critical as we could substitute it for preset tests and not integrate the targetted tests. However, we believe that as this project is a tutor, we should give the user targetted tests to highlight their flaws so they can fix them as soon as possible.
**Dependencies with other requirements**
This depends on all the above requirements as to create the data sets required to have this functionality we must have all the input working correctly

### *3.7 Accounts and Data storage*
**Description**
This functionality will manage all of the storing and retrieval of user data. We will have users sign up by giving us a username and password. Once they have then we will store their typing related data, their username, userID and their password to our database.
**Criticality**
This functionality is not critical as it is only necessary if we plan on users signing in and out. If you eliminate this functionality then the product will still work perfectly fine and will still provide a great user experience
**Dependencies with other requirements**
This depends on the resulting feedback as this result feedback will also be stored for later reference to make prompts when the user signs back in.

### *3.8 Web app integration*
**Description**
This is last on this list as we deem it the least important function of the project. This is the outer scope of our project. We hope to integrate a working branch of the project we flask and have the application hosted on the web.
**Criticality**
This is the least critical aspect of our project. Nothing relies on this to work and we are still unsure if we will be able to get this into the final product but it something that we are certainly aiming to achieve.
**Technical issues**
Taking input from the webcam and doing all of our calculations with the performance constraints of a flask web app may cause some severe slowdown issues.
**Dependencies with other requirements**
To create a python web app with flask will depend on nothing mentioned above but to have our fully-fledged project available as a web app then the web app will be dependant on all functionalities mentioned above

---
## 4. System Architecture
![System Architecture Diagram](https://i.imgur.com/xOXKqwo.png)

The above diagram is a basic layout of our planned architecture. It shows how the program will take input from both the user typing on the keyboard and the camera taking snapshots of the user typing. The images taken by the camera are given to OpenCV to process. The program also has to send and receive data form the database for creating, receiving and updating data.



---
## 5. High-Level Design
![](https://i.imgur.com/4ugWUmv.png)

This diagram shows how data should be passed around the system, assuming the user already has an account. It begins with the user signing in and the retrieval of their data form previous exercises. Next, a tutorial is generated from this data and given to the user to complete. In the case of a brand new account, a generic "all round" tutorial is created. After the tutorial is finished, data form the camera and keyboard are taken to create the final result of the tutorial. This is displayed back to the user and also added to their data. The user is then given an option to begin a new tutorial. If they agree, the next tutorial is generated (this is shown in the diagram as "New tutorial"). If not, the user signs out and their data is updated in the database.

---
## 6. Preliminary Schedule
![GANTT chart](https://i.imgur.com/9CliRu1.jpg)

---
## 7. Appendices

7.1 Touch-typing finger layout example ![touch typing finger layout example](https://miro.medium.com/max/1514/0*gtN8lOemEF_7I5bb.png)