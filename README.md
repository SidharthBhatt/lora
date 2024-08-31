**Intro:** 

Ever touched grass and wondered what animals were around you? Probably not considering your reading this, but the vast majority animals wouldn't be too thrilled to meet you either. Limited cell service, SD cards are too time intensive, and wifi's range is too limited. Introducing a unique trail camera featuring a lora rasberry pi hat PCB and worlds first open source lora video streaming protocol written in python. I literally wrote the code so an image can be converted into bytes, turned into radio frequencies, and subsequently decoded up to 2 miles away. Images take less than a minute to be sent and can be sorted with a modified version of PyTorch Wildlife. 

**Motivation:**

Really wanted to do a big project (after doing many small ones) and this one was accessible, interesting, and made the world a better place. I took a prototype of this on Hackclub's the trail.

**Challenges:**
- didn't know what a pcb was -> learned how to use easyeda
- first pcb had the wrong ipex connector -> bought new ipex connector
- first pcb's moduels came dead on arrival -> created second pcb
- second pcb had a component in the wrong orientation -> individually desodered a 40 pin header, broke it, and resodered only the metal bits that were needed
- webcam drivers weren't working -> used ffmpeg
- base64 encoding wasn't working -> used pil library
- some packets were being missed  -> increased wait time between packets
- didn't know ML -> took multivariable calculus, linear algebra, and taught middle schoolers ML (teaching others is the best way to learn)
- didn't know anything about ML research -> started with YOLO and read original paper & googled everything I didn't know

**TLDR: Worked really hard (5k+ lines of code), learned everything from PCB design to ML, and made a unique project.**


**How it works:**

![image](https://github.com/user-attachments/assets/f6232446-1c0b-4e67-a044-f8bd973873ba)

![image](https://github.com/user-attachments/assets/23649afb-30c7-4c5a-811a-5a3ec9e80eb4)

![image](https://github.com/user-attachments/assets/9380932b-402d-43e7-a354-f009e1f05b4b)

![image](https://github.com/user-attachments/assets/e0fd9485-2fad-4289-b185-7ba308102eab)

![image](https://github.com/user-attachments/assets/5b674318-ba81-40cc-a534-95e72daca2bd)



WARNING: This project is in a highly active state of development and subject to change at any point in time. 

Copyright 2024 @SidharthBhatt

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
