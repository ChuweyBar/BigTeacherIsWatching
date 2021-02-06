# BigTeacherIsWatching
HackInPlace Feb2021 Project

<h1> Objective </h1>
<p>
    This project was done for the Hack in Place Hackathon. There were four challenges available: Home, Economy, Health, and Education.
</p>

<h2> Description of the four challenges: </h2>
<h3> Home </h3>
<p>
    2020 saw record-breaking wildfires, heatwaves, hurricanes, and floods. The increasing severity of natural disasters is just one facet through which climate chnage is affecting our one home - planet earth. 

    Team Challenge: Create innovative solutions that help individuals reduce their carbon footprint, and become more resilient to changes in the environment. 
</p>

<h3> Economy </h3>
<p>
    Extended shelter-in-place restrictions, necessitated by the pandemic, have led to significant financial losses for most small and medium-sized businesses, forcing many to permanently close down altogether. 

    Team Challenge: Design resourceful methods to help local businesses connect and engage with consumers in the COVID era. 
</p>

<h3> Health </h3>
<p>
    Even with the ongoing vaccine rollout, the COVID pandemic is still a huge health risk both to us and our communities.

    Team Challenge: Find creative ways for people to stay resilient and healthy both mentally and physically while sheltering in place.
</p>

<h3> Education </h3>
<p>
    Systems of education are always evolving, but last year we saw drastic changes in how we learn. While we’ve made good progress in transitioning to online learning, there still remains much to be done in this space.

    Team Challenge: Find ways that we can improve the virtual learning experience for learners and instructors
</p>

<h4> Team Choice </h4>
<p> 
    Our team was originally stuck between the theme of Education and Home. Specifically, the issues of climate change and carbon footprint tracking from Home and the anti-cheating mechanism for Education. We ultimately elected to pursue the theme of Education. During the COVID pandemic and the transition to online learning, there has been an increase in academic dishonesty accusations and cheating. But, this already has a solution technologically with lockdown browsers and proctoring during live exams. However, the biggest issue of all was the difficulty in transition from a physical classroom experience to an fully online classroom experience.
</p>

<p>
    Many professors noted that their students did worse during the online setting. In addition, many teachers were not able to fully gauge their student's level of understanding of the material. This can perhaps be due to a lack of attention during classtime.
</p>

<p>
    To address the above possibility and issue, we decided to create a rather dystopian solution. Our prototype can serve as an additional feature on Zoom, where student's eyes will be tracked. If they look away, it will be flagged and perhaps, the professor can come back to review these moments. This can give the professor a sense of when a student lost focus and what can potentially be reviewed in the coming days.
</p>

Pupil Tracking 

The software 1984 provides a solution for online teachers to track students’ attention through OpenCV eye tracking.

The algorithm uses existing face_cascade and eye_cascade classifiers to identify students’ face and eyes on camera. The following is the algorithm explanation:

![alt text](img1.jpg)

When a face is detected, the algorithm searches for eyes on the top half of the face roi. This reduces chances of mismatching the mouth as an eye. However it can be reversed if we receive complaints about discriminating against people with enormous foreheads.

![alt text](img2.jpg)

After eyes are located in the top half of the face, The algorithm divides the face into left and right sections to separate the right and left eye. (Left and right is subjective here)

![alt text](img3.jpg)

Once the eyes are located, the algorithm moves on to determine the pupil’s location relative to where the eye is. The algorithm collectes the average position of the pupil every 20 seconds and determine if the student is current on task or not.

