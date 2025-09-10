# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def active(event, name, interact=True, **kwargs):
        global current_speaker
        if not interact:
            return

        if event == "begin":
            current_speaker = name

default current_speaker = None

define mainchar = Character("[povname]", image='mainchar', callback=active, cb_name='mainchar')
define maincharn = Character("", image='mainchar', callback=active, cb_name='maincharn') # char name with n behind are just the char with no name

define kalifer = Character("Dr.Kalifer", image='kalifer', callback=active, cb_name='kalifer')
define kalifern = Character("", image='kalifer', callback=active, cb_name='kalifern')

define chen = Character("Xi Chen", image='chen', callback=active, cb_name='chen')
define chenn = Character("", image='chen', callback=active, cb_name='chenn')

define eileen = Character("Eileen", image='eileen', callback=active, cb_name='eileen')
define eileenn = Character("", image='eileen', callback=active, cb_name='eileenn')

define meng = Character ("Shang Meng", image='meng', callback=active, cb_name='meng')
define mengn = Character ("", image='meng', callback=active, cb_name='mengn')

define phone = Character ("Phone", image='phone', callback=active, cb_name='phone')

define n = Character("",callback=active,cb_name='n')

define sDream = 5
define occupation = 0

# Define the images for characters with ConditionSwitch to handle the current speaker highlighting
image mainchar = ConditionSwitch(
    "current_speaker == 'mainchar'", "images/mainchar.png",
    "current_speaker == 'maincharn'", "images/mainchar.png",
    "current_speaker != 'mainchar'", im.MatrixColor("images/mainchar.png", im.matrix.saturation(0.4) * im.matrix.brightness(-0.2))
)

image chen = ConditionSwitch(
    "current_speaker == 'chen'", "images/chen.png",
    "current_speaker == 'chenn'", "images/chen.png",
    "current_speaker != 'chen'", im.MatrixColor("images/chen.png", im.matrix.saturation(0.4) * im.matrix.brightness(-0.2))
)

image kalifer = ConditionSwitch(
    "current_speaker == 'kalifer'", "images/kalifer.png",
    "current_speaker == 'kalifern'", "images/kalifer.png",
    "current_speaker != 'kalifer'", im.MatrixColor("images/kalifer.png", im.matrix.saturation(0.4) * im.matrix.brightness(-0.2))
)

image eileen = ConditionSwitch(
    "current_speaker == 'eileen'", "images/eileen.png",
    "current_speaker == 'eileenn'", "images/eileen.png",
    "current_speaker != 'eileen'", im.MatrixColor("images/eileen.png", im.matrix.saturation(0.4) * im.matrix.brightness(-0.2))
)

image meng = ConditionSwitch(
    "current_speaker == 'meng'", "images/meng.png",
    "current_speaker == 'mengn'", "images/meng.png",
    "current_speaker != 'meng'", im.MatrixColor("images/meng.png", im.matrix.saturation(0.4) * im.matrix.brightness(-0.2))
)

# The game starts here.

label start:

    scene campusway with fade
    play music "audio/sleep.mp3" fadeout 1.0 fadein 3.0 loop
 
    n"'A sunny day on campus, students are seen celebrating their graduation.'"

    n"'At this exciting moment, a young student seems to be a bit... out of Place'"

    n"'...Because he was lying on the ground and looked like he was not in good condition.'"

    show mainchar with dissolve

    maincharn "......"

    maincharn "What just happened..."

    hide mainchar with dissolve

    show chen with dissolve

    chenn "Are you okay? "

    chenn "You just passed out for a moment... Can you still get up?"

    hide chen with dissolve

    show mainchar at left with dissolve

    show chen at right with dissolve

    maincharn "I think I can..."
    
    chenn "Take it easy, your ankle might be sprained."

    chenn "There you go."

    maincharn "I think I should be fine..."

    chenn "You sure you dont need any help?"

    maincharn "I was just too tired, some rest will do. May I know your name, sir?"

    chenn "You can call me Mr.Chen, here is my business card."

    n"'The card looks very nice, with a speckled and rippled surface that gives it a subtle, but stylish and elegant look.'"

    n"'At a very prominent location, you noticed the name of the owner -- Xi Chen'"

    chen "I was a bit late for the graduation ceremony, but I heard part of your speech."

    chen "It was very interesting and I believe that your area of study matches our company's needs."

    chen "So by any chance if you are interested, come by my office and we can have a chat. What's your name?" 
    $ povname = renpy.input("My head is still a bit dizzy... What was my name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Alex"

    mainchar "Thanks for the compliment Mr.Chen, my name is [povname]. I will take your suggestion into my future considerations."

    chen "Very well, I have another event I need to attend soon. Enjoy your graduation and remember to rest well when you need to."

    mainchar "Thank you Mr.Chen, have a nice day!"

    hide chen with dissolve

    mainchar "......"

    mainchar "Maybe I should get some rest..."

    show meng at right with dissolve

    n"All of a sudden, you felt a cold touch on your face."

    n"When you turn your eyes at the object at your face, you saw a can of soft drink."

    n"And a familiar voice came from your side..."

    mengn "What is our future PHD doing over here? Thinking on a significant project?"

    n"You quickly realized that she is your old friend Shang Meng, you've known each other since primary school."

    n"Taking the drink she just gave you, the icy touch made your mind more conscious"

    mainchar "Not exactly... Just considering a job opportunity here, someone just hands me a business card and said that their company might need me."

    meng "But isn't your plan after graduation to get a master degree? Then you can fight for your PHD degree after?"

    n"Shang Meng seems to be a bit worried of you, she quickly put her hand in front of your forehead."

    meng "It doesn't seem like you had fever, then why are u a bit tripping?"

    mainchar "Meng, I was serious. I don't know when does this idea starts to pop in my mind..."

    mainchar "But I do sometimes think that maybe a job might be a better fit for my situation."

    meng "I mean, it really is up to you... But I also don't want to see you making compromising on your dream..."

    meng "I am always by your side, no matter what your decision is."

    n "Seeing Shang Meng like this, you can't help but reach out and pet her head."

    mainchar "That is why I am still considering about all the possible paths, don't worry I will choose wisely."

    mainchar "I will make a choice that I will never regret."

    meng "Good to know~ I don't wanna see you regret about picking the wrong path and cry like a young baby."

    mainchar "......"

    mainchar "You know I won't."

    meng "And you know that was just a joke..."

    meng "That's more like you... Dull as always."

    meng "Anyways, that's a lot of talking. The evening is drawing near, I'm hungry, do you want to join me for a early dinner?"

    menu:
        "Join her":
            mainchar "Sure, I felt that I am a bit hungry too. Where should we go?"

            meng "Let's leave a touch of mystery, I know the perfect place to go."

            mainchar "......After you, my lady."
            $ sDream = sDream + 2
            jump dinner
        "Refuse her":
            mainchar "Hmmm... I am not too hungry at the moment, I might just walk around the campus for bit longer and take some pictures."

            mainchar "Since it might be the last time to see this beautiful place."

            meng "Alright, have fun with the campus view~ Don't forget to send me some of those pictures as well."

            hide meng with dissolve
            $ sDream = sDream - 1

            jump friend

    label dinner:
        scene cafe with fade
        play music "audio/moon.mp3" fadeout 1.0 fadein 3.0 loop

        show meng at right with dissolve

        show mainchar at left with dissolve 

        meng "Ta-da~ Welcome to Alan's cafe~ I love the pasta here so much, this is my favourate place to eat."

        mainchar "......I thought your favourate restaurant is jzou BBQ."

        meng "I mean it was, untill I found this place a few weeks ago. It was such a wise decision to seek out for food during exam period."

        mainchar "Something you would do... But don't you worry about your exams? I heard that Dr.Kalifer got some real tough questions for this semester's exam."

        meng "Aren't you in the same course as well? I know you would never miss any of his course."

        mainchar "You know that's not really a problem for me. I stay up all night somedays during the exam week for review."

        meng "But I did the review as well..."

        n "Shang Meng was about to say something, but she immediatly noticed that you are rolling your eyes."

        meng "?"

        n "Then you felt a sudden pain on your cheek."

        meng "WHAT ARE YOU TRYING TO SAY?"

        mainchar "Ahahah, my bad, my bad. I am not trying to say anything."

        n "After glared at you for a second, Shang Meng let go of her hand."

        mainchar "......Kalifer's questions are a bit hard, but not really tricky. Wouldn't be a big deal for you, would it?."

        meng "I got a A- in the end, not too bad I guess."

        mainchar "Not bad at all, wait isn't that Dr.Kalifer?"

        meng "Well you are lucky isn't it? It would be a nice time to chat with him about your future plan. Do you want me to pick your food?"

        mainchar "Sure, like always."

        hide meng with dissolve

        mainchar "Hi, Dr.Kalifer!"

        show kalifer at right with dissolve

        kalifer "Hi [povname], happy graduation. How was your day?"

        mainchar "Not bad, just wondering about the future plan. Do you think it would be a good idea that I just go ahead and give it a try for a master degree?"

        n "Dr.Kalifer sits infront of you, the coffee mug in his hand is still steamy, with a special smell of roasted coffee beans."

        kalifer "Sure we can talk about it. What are you currently thinking about? In general."

        mainchar "I do have a few thoughts before...... But now when I am actually at one of the crossroads of my life my mind is a bit messed up."

        kalifer "Don't worry, you still have time left before the deadline. You should rest a bit before you actually make the decision."

        kalifer "Let's say that you are going to get a master degree. You grade is good enough and I can tell you have certain knowledge with some good understanding in your area of study."

        kalifer "So you don't need to worry that you won't be able to get a master degree. And if you wish I can be your supervisor or I can find someone that worth to trust."

        kalifer "Thus it's really up to you at the point. There won't be much of the trouble if you wish to continue to graduate school."

        kalifer "But also if you felt more comfortable to get a job or doing something else, that is totally fine."

        mainchar "......"

        mainchar "'Should I actually continue to graduation school?'"

        menu:
            "Continue to graduation school":
                $ occupation = 1
                mainchar "......"
                mainchar "Dr.Kalifer, I have now decided. I want to proceed to graduate school. Do you mind to be my supervisor?"

                kalifer "Sure thing, since you have decided to proceed to a master degree. Come to my office when you have some time next week, I have a few research projects and research directions you might be interested in."
                mainchar "Thank you so much Dr.Kalifer."
                kalifer "Alright, very well. Enjoy your meal, and I will see you next week."
                
                hide kalifer with dissolve
                mainchar "......"
                mainchar "Even that I made a decision here, still feels a bit... wired?"

  

            "Think about it some more":
                mainchar "I think you are right, Dr.Kalifer. I should think about it some more."
                kalifer "Sure thing, like what I said, you always have time to take a rest and decide. Make sure to follow your actual thoughts."
                kalifer "And if that you end up with proceeding to graduate school, come to my office when you have time. I have a few research projects and research directions you might be interested in."
                mainchar "Thank you so much Dr.Kalifer."
                kalifer "Alright, very well. Enjoy your meal."

                hide kalifer with dissolve
                mainchar "......"
                mainchar "It's always good to be cautious, isn't it?"

        show meng at right with dissolve
        meng "What did Dr.Kalifer said?"
        mainchar "I just talked to him with the graduation school plan."
        mainchar "I think I should read more papers at this point to get better understanding, and..."

        n "Shang Meng stoped your words by putting her index finger on top of your lips"

        meng "Shhhh... It's dinner time we don't talk about academic or work topics. You really need to learn to take a brake sometime. Especially when you really need it."
        mainchar "But I don't really felt tired?"
        meng "That's just because your are too nervous about this decision. Your mental has been tight like a bow's string for the past few years, if you don't learn when and how to take a break..."
        meng "...You will 'break' yourself."
        mainchar "......You are right."

        jump phonea

    label friend:
        mainchar "......"
        mainchar "Maybe I should go visit Dr.Kalifer later in the day to get some suggestions."
        n "The sun casts a warm glow on the lush greenery, illuminating the vibrant leaves and delicate petals."
        n "Tall trees provide dappled shade, while colorful flowers bloom along the pathways."
        n "A few students walking by, with their happiness on the face."
        n "You took a few picture with your phone, as a little souvenir before the potential farewell to the campus."
        n "Right after you finished sending the picures to Shang Meng, you felt a hand on your shoulder."

        show eileen at right with dissolve
        eileenn "Happy graduation [povname], what are you doing here?"
        n "The memory between you and the owner of the voice quickly pop up in your mind."
        n "He is your friend and classmate, one of Dr.Kalifer's favourate students. Known by good at computer science related subjects."
        n "Though you are not in a very close relation but sometimes you do hang out or working on some projects together."
        mainchar "Eileen? I was just walking around, you know. This might be the last time to see this view."
        mainchar "What about you?"
        eileen "I wish I could have a moment to sit down and relax as well... Anyways, I was busy on inviting the graduates to my company."
        mainchar "......"
        mainchar "You own a company?"
        eileen "Just a start up, many positions are empty right now and I really need to hire more people......"
        n "All of a sudden, it feels like he just suddenly realized something. He quickly went in front of you in a very close range."
        eileen "How can I forgot about you? You have not accept any job offers yet right?"
        mainchar "So far yes."
        eileen "Do you want to join my company? With your ability, we can actually make something big."
        eileen "You can be one of the founders, and we can discuss the details later."
        mainchar "......I can take that into consideration."
        eileen "This might not be a good place to talk, you want to come to my house? We can have a little dicussion of the details."
        menu:
            "Accept":
                mainchar "Sure, why not."
            "Refuse":
                n "You were going to refuse him, but all of a sudden you realized that you forgot to bring the key with you today."
                n "And you are not sure when will Shang Meng be home today."
                mainchar "Sure, why not."

        scene ehouse with fade
        play music "audio/house.mp3" fadeout 1.0 fadein 3.0 loop
        n "Eileen's place wasn't really far away from the campus, thus it only took you around ten minutes to walk over.    "
        show eileen at right with dissolve
        show mainchar at left with dissolve
        eileen "Take a seat, do you want some tea?"
        mainchar "Sure."
        n"After sitting down, you start to look around the house."
        n"You have to admit, though Eillen seem to be careless to the small details that does not matter too much..."
        n"But in fact he does care about those details, as the room of his is well orgnized and clean."
        eileen "Here goes your tea."
        n"While your were waiting and looking around. Eileen quickly brew a cup of green tea with the hot water stored in the water machine."
        n"Though it seem pretty stright forward, but you noticed the ordering of his process is different from what you usually to brew the tea."
        mainchar "The tea is very nice."
        eileen "I got it from China, it takes a bit of progress to get it here. But I believe it's worth the trouble."
        mainchar "I'm sure it does. So, what is the project that you are planing to do?"
        eileen "We are trying to build an AI butler for our potential customers."
        eileen "So that it can be a reliable secretary handeling schedule, sending out food order, taking notes from meeting and many other features we are going to add as we go."
        n"While listening, you took a sip at the tea in front of you. It has high and intensive aromanow and now you understand why it would be worth the trouble."
        mainchar "So where are you currently at?"
        eileen "We have finished the base structure, now we really need to use data and cases to train the model."
        eileen "I believe that is what you are good at?"
        mainchar "Though I am not bad with it, but it will still take a very long time to do so. Are you sure everything else during the period can be handeled by others?"
        eileen "If you can train the model, I can take care of the rest."
        menu:
            "Join Eileen's Company":
                $ occupation = 2 
                mainchar "......"
                mainchar "Alright, I'm in."
                eileen "Nice! Here is my business card with the adress of our office. You can come by next week and I will get your things onboard."
                mainchar "Can I start the trainning now?"
                eileen "They are still wrapping up with the base model."
                mainchar "But you told me...... I guess its too late to realize."
                eileen "Just consider it as a small break before the hard work. You might not get a chance to rest well after we start."
                mainchar "I guess so."
            "Think about it some more":
                mainchar "......"
                mainchar "I need to think about it some more."
                eileen "That's fine, take your time. This is not a easy decition."
                eileen "Our developmen of the base model is still wrapping up, so we are not in a rush."
                eileen "Let me know by next week if you decide to join or not."
                eileen "And here is my business card with the adress of our office. You can come by and take a look if you are interested."
                mainchar "Thanks."

        n "After that you and Eileen chatted a few more interesting topics and enjoyed a few more cups of the tea."
        mainchar "I will have to leave, before Shang Meng went to sleep and then no one will open the door for me."
        eileen "Oh I see, do you need me to drive you?"
        mainchar "No thanks, I got my car in the campus parking lot."
        eileen "Ok, have a nice one."
        mainchar "Thanks for the tea."
        eileen "You are welcome."
        hide mainchar with dissolve
        jump phoneb

    label phonea:

        scene home with fade
        play music "audio/house.mp3" fadeout 1.0 fadein 3.0 loop
        show meng at right with dissolve
        show mainchar at left with dissolve
        meng "Home sweet home."
        mainchar "......You never ran out of energy."
        meng "What do you mean... I do get tired as well."
        meng "I am going to take a shower if you don't mind, then you can do it after."
        mainchar "Isn't it always how the shower order goes? Lady's first."
        meng "Do you want me praise you as a gentleman?"
        mainchar "No thank you."
        hide meng with dissolve
        n "When you were about to sit on the seat and stare at the outside view, a sudden ring appears on your phone."
        n "And the name appears with the phone number is 'Eileen'."
        n "The memory between you and the owner of the voice quickly pop up in your mind."
        n "He is your friend and classmate, one of Dr.Kalifer's favourate students. Known by good at computer science related subjects."
        n "Though you are not in a very close relation but sometimes you do hang out or working on some projects together."
        hide mainchar with dissolve
        show phone at center with dissolve
        eileen "Happy graduation [povname], how are you?"
        mainchar "Eileen? Oh I just got home from the campus, not much to do and just chilling here. What's up?"
        eileen "That's nice.. I wish I could have a moment to sit down and relax as well."
        eileen "Anyways, I hope I did not bother you too much here. I am here to invite you to my company."
        mainchar "......"
        mainchar "You own a company?"
        eileen "Just a start up, many positions are empty right now and I really need to hire more people......"
        eileen "Do you want to join my company? With your ability, we can actually make something big."
        eileen "You can be one of the founders, and we can discuss the details later."
        mainchar "Interesting... Tell me more about it."
        eileen "Sure! We are trying to build an AI butler for our potential customers."
        eileen "So that it can be a reliable secretary handeling schedule, sending out food order, taking notes from meeting and many other features we are going to add as we go."
        mainchar "Where are you currently at?"
        eileen "We have finished the base structure, now we really need to use data and cases to train the model."
        eileen "I believe that is what you are good at?"
        mainchar "Though I am not bad with it, but it will still take a very long time to do so. Are you sure everything else during the period can be handeled by others?"
        eileen "If you can train the model, I can take care of the rest."
        if occupation == 0:
            menu:
                "Join Eileen's Company":
                    $ occupation = 2
                    mainchar "......"
                    mainchar "Alright, I'm in."
                    eileen "Nice! I will send you the adress of our office. You can come by next week and I will get your things onboard."
                    mainchar "Can I start the trainning now?"
                    eileen "They are still wrapping up with the base model."
                    mainchar "But you told me...... I guess its too late to realize."
                    eileen "Just consider it as a small break before the hard work. You might not get a chance to rest well after we start."
                    mainchar "I guess so."
                "Think about it some more":
                    mainchar "......"
                    mainchar "I need to think about it some more."
                    eileen "That's fine, take your time. This is not a easy decition."
                    eileen "Our developmen of the base model is still wrapping up, so we are not in a rush."
                    eileen "Let me know by next week if you decide to join or not."
                    eileen "I will send you the adress of our office. You can come by and take a look if you are interested."
                    mainchar "Thanks."
        else:
            menu:
                "Think about it some more":
                    mainchar "'Maybe I have made my choice too early...'"
                "Think about it some more":
                    mainchar "'Maybe I have made my choice too early...'"
            mainchar "I need to think about it some more."
            eileen "That's fine, take your time. This is not a easy decition."
            eileen "Our developmen of the base model is still wrapping up, so we are not in a rush."
            eileen "Let me know by next week if you decide to join or not."
            eileen "I will send you the adress of our office. You can come by and take a look if you are interested."
            mainchar "Thanks."
        n "After that you and Eileen chatted a few more interesting topics and you had a great time chatting."
        eileen "I will have to go, I had a meeting scheduled with the other company in China."
        mainchar "Alringht, nice chatting with you. Good luck with your meeting."
        eileen "Thanks, talk to you later."
        hide phone with dissolve
        show mainchar at left with dissolve
        mainchar "......"
        show meng at right with dissolve
        meng "How was the little break?"
        mainchar "Not bad."
        jump dream

    label phoneb:

        scene home with fade
        play music "audio/house.mp3" fadeout 1.0 fadein 3.0 loop
        show meng at right with dissolve
        meng "Where did you go? That's a bit too long for a campus tour."
        show mainchar at left with dissolve
        mainchar "A friend of mine shared some interesting thing with me."
        mainchar "Do you know Eileen?"
        meng "That computer science student you mentioned before? I remember you were saying he has some decent skills."
        mainchar "He creates a company and try to invite me in. The plan is solid and I think the goal is achievable."
        mainchar "Anyways, how was your dinner?"
        meng "Not bad, that store is at that good location for a reason."
        n "Right at the momen meng was going to say something else, a sudden ring appears on your phone."
        n "And the name appears with the phone number is 'Dr. Kalifer'."
        meng "I'm going to get on my game account for the daily missions. Have fun~"
        hide meng with dissolve
        mainchar "......"
        mainchar "Hi, Dr.Kalifer!"
        hide mainchar with dissolve
        show phone at center with dissolve
        kalifer "Hi [povname], happy graduation. How was your day?"
        mainchar "Not bad, just wondering about the future plan. Do you think it would be a good idea that I just go ahead and give it a try for a master degree?"

        kalifer "Sure we can talk about it. What are you currently thinking about? In general."

        mainchar "I do have a few thoughts before...... But now when I am actually at one of the crossroads of my life my mind is a bit messed up."

        kalifer "Don't worry, you still have time left before the deadline. You should rest a bit before you actually make the decision."

        kalifer "Let's say that you are going to get a master degree. You grade is good enough and I can tell you have certain knowledge with some good understanding in your area of study."

        kalifer "So you don't need to worry that you won't be able to get a master degree. And if you wish I can be your supervisor or I can find someone that worth to trust."

        kalifer "Thus it's really up to you at the point. There won't be much of the trouble if you wish to continue to graduate school."

        kalifer "But also if you felt more comfortable to get a job or doing something else, that is totally fine."

        mainchar "......"

        if occupation == 0:
            menu:
                "Continue to graduation school":
                    $ occupation = 1
                    mainchar "......"
                    mainchar "Dr.Kalifer, I have now decided. I want to proceed to graduate school. Do you mind to be my supervisor?"
                    kalifer "Sure thing, since you have decided to proceed to a master degree. Come to my office when you have some time next week, I have a few research projects and research directions you might be interested in."
                    mainchar "Thank you so much Dr.Kalifer."
                    kalifer "Alright, very well. Have a good night and I will see you next week."
                
                    hide phone with dissolve
                    show mainchar at left with dissolve
                    mainchar "......"
                    mainchar "Even that I made a decision here, still feels a bit... wired?"  

                "Think about it some more":
                    mainchar "I think you are right, Dr.Kalifer. I should think about it some more."
                    kalifer "Sure thing, like what I said, you always have time to take a rest and decide. Make sure to follow your actual thoughts."
                    kalifer "And if that you end up with proceeding to graduate school, come to my office when you have time. I have a few research projects and research directions you might be interested in."
                    mainchar "Thank you so much Dr.Kalifer."
                    kalifer "Alright, very well. Have a good one."

                    hide phone with dissolve
                    show mainchar at left with dissolve
                    mainchar "......"
                    mainchar "It's always good to be cautious, isn't it?"
        else:
            menu:
                "Think about it some more":
                    mainchar "I think you are right, Dr.Kalifer. I should think about it some more."
                "Think about it some more":
                    mainchar "I think you are right, Dr.Kalifer. I should think about it some more."
            kalifer "Sure thing, like what I said, you always have time to take a rest and decide. Make sure to follow your actual thoughts."
            kalifer "And if that you end up with proceeding to graduate school, come to my office when you have time. I have a few research projects and research directions you might be interested in."
            mainchar "Thank you so much Dr.Kalifer."
            kalifer "Alright, very well. Have a good one."

            hide phone with dissolve
            show mainchar at left with dissolve
            mainchar "......"
            mainchar "Maybe it is not a good idea to decide too early?"

        show meng at right with dissolve
        meng "How was the little talk?"
        mainchar "Not bad."
        jump dream
    
    label dream:
        play music "audio/midnight.mp3" fadeout 1.0 fadein 3.0 loop
        meng "Do you have a plan tomorrow? I'm planning to visit the theme park that just got completed near the downtown."
        mainchar "I don't but......"
        meng "Then you don't have the right to refuse."
        meng "Its a good opportunity to relax your mental."
        mainchar "Maybe I should say I do have a plan..."
        meng "Does it felt that bad to hang out with me?"
        mainchar "I didn't mean it that way......"
        meng "Anyways, take a good sleep and we will go whenever you are up."
        mainchar "Shouldn't we go early to avoid the crowd?"
        meng "I bought the premium pass for us, so that we don't have to queue."
        mainchar "That's convenient."
        meng "Good night."
        hide meng with dissolve
        mainchar "Good night."

        jump park

    label park:

        scene park with fade
        play music "audio/park.mp3" fadeout 1.0 fadein 3.0 loop
        show meng at right with dissolve
        meng "We are lucky~ The weather is very good today."
        $ sDream = sDream + 3
        show mainchar at left with dissolve
        mainchar "......"
        meng "Come on, it's a good day to have fun. Don't be like that."
        mainchar "I'm fine, just didn't sleep too well last night."
        meng "I thought you woke up without a alarm, did you rest well?"
        mainchar "Not sure, still a bit not concious."
        meng "I'm sure that inside of that gate there will be something to turn you on."
        meng "Here, have some water that I just got over there."
        mainchar "Thanks."

        scene park2 with fade
        show meng at right with dissolve
        show mainchar at left with dissolve
        meng "Feeling better?"
        mainchar "A little bit, that tea cup was interesting."
        meng "Seem like you have warmed up already~"
        mainchar "Could be more ready if you did not spin the wheel in the middle that fast..."
        meng "That's part of the warm up~"
        mainchar "My head was still a bit dizzy..."
        meng "Be strong my friend, the journey just starts~ Come on, let's go."
        hide meng with dissolve
        mainchar "......"
        hide mainchar with dissolve

        scene train with fade
        show meng at right with dissolve
        show mainchar at left with dissolve
        meng "[povname], look! That train-like roller coaster looks fun, let's go try that!"
        mainchar "......"
        mainchar "You kidding, right?"
        meng "Nice try."
        mainchar "......"
        mainchar "Is it too late to go home and take a second nap?"
        meng "Yes it is, let's go and have some fun with that roller coaster~"
        mainchar "Why did I say yes to this theme park idea first place......"

        scene train with fade
        show meng at right with dissolve
        meng "Hum hum, that was fun~"
        meng "What do you think, [povname]?"
        meng "[povname]?"
        show mainchar at left with dissolve
        mainchar "......"
        mainchar "......I"
        mainchar "...I think I am going to throw up..."
        meng "Are you ok?"
        meng "You don't seem ok..."
        meng "Stay here, I will go grab some water for you."

        scene train with fade
        show meng at right with dissolve
        show mainchar at left with dissolve
        meng "Feeling better?"
        mainchar "......"
        mainchar "Better..."
        meng "Are you sure you are fine?"
        meng "I'm sorry, I shouldn't drag you to that..."
        mainchar "That's ok."
        mainchar "I just need some time to relax."
        meng "......"
        mainchar "Don't be like that, I'm not dying."
        meng "I just..."
        mainchar "I understand, you just want me to enjoy the time here."
        mainchar "Not your fault."
        meng "But..."
        mainchar "Go play a few more facilities, I will be waiting here."
        meng "Why would I? We are here to make you feel better."
        meng "I didn't make you feel better and even made you sick..."
        mainchar "That's ok, I will join you shortly."
        mainchar "These tickets are not cheap, let's get the money's worth."
        mainchar "It won't take long for me to recover."
        mainchar "Go find a few facility that are not that tough for me."
        mainchar "So that we can enjoy together."
        meng "......Ok, if you felt bad or you need me jus make a phone call."
        mainchar "Have fun."
        meng "See you in a bit..."
        hide meng with dissolve

        scene park2 with fade
        show mainchar at left with dissolve
        mainchar "......"
        mainchar "Where is Meng now... I think she went this way."
        n "Suddenly, a man with a nice suit appears in your sight."
        mainchar "Mr. Chen? Didn't expect to see you here."
        show chen at right with dissolve
        chen "Oh hi [povname], how you doing?"
        mainchar "Not bad, had a bit of fun here. The facilities are very interesting."
        chen "Good to know, I'm here with my family. They are having so much fun with the roller coaster."
        chen "Have you try that yet?"
        mainchar "......"
        mainchar "It was... fun."
        chen "Sounds like you had some interesting moment up there. How were you thinking of the job offer?"
        chen "We have currently started a new project and we need people like you, who are good at training AI model."
        if occupation == 0:
            menu:
                "Accept the offer":
                    $ occupation = 3
                    mainchar "Sure Mr. Chen, I will take the offer."
                    mainchar "Thanks for providing this oppertunity."
                    chen "No problem, you have my business card. See me at my office next week, I will get you onboard."
                    chen "Looking forward to see you around."
                    mainchar "Thanks Mr. Chen, see you then."
                    chen "Have a good one."
                    mainchar "You too."

                "Think about it more":
                    mainchar "Sorry Mr. Chen, I need some more time to think about it."
                    chen "Oh my friend no need to oppologize. Sorry for mentioning this while you were trying to enjoy your time here."
                    chen "The offer always stands, if you have decide just come by my office and I will get your things onboard."
                    mainchar "Thanks Mr. Chen. For offering such an opportunity."
                    chen "No problem, enjoy your time here."
                    mainchar "You too."
        else:
            menu:
                "Think about it more":
                    mainchar "'I can't accept the order here...... Maybe I have made the decision too early'"
                    mainchar "Sorry Mr. Chen, I need some more time to think about it."
                    chen "Oh my friend no need to oppologize. Sorry for mentioning this while you were trying to enjoy your time here."
                    chen "The offer always stands, if you have decide just come by my office and I will get your things onboard."
                    mainchar "Thanks Mr. Chen. For offering such an opportunity."
                    chen "No problem, enjoy your time here."
                    mainchar "You too."
                "Think about it more":
                    mainchar "'I can't accept the order here...... Maybe I have made the decision too early'"
                    mainchar "Sorry Mr. Chen, I need some more time to think about it."
                    chen "Oh my friend no need to oppologize. Sorry for mentioning this while you were trying to enjoy your time here."
                    chen "The offer always stands, if you have decide just come by my office and I will get your things onboard."
                    mainchar "Thanks Mr. Chen. For offering such an opportunity."
                    chen "No problem, enjoy your time here."
                    mainchar "You too."
        hide chen with dissolve
        mainchar "What a coincidence..."
        mainchar "Didn't expect to see Mr. Chen here..."

        show meng with dissolve
        play music "audio/midnight.mp3" fadeout 1.0 fadein 3.0 loop
        meng "Where did you go? Did you feel better?"
        mainchar "Just walking around trying to find you."
        mainchar "I feel much better now, what did you find during the time?"
        mainchar "Anything at my level?"
        meng "Certainlly, for example the ......"
        n "After that, you and Shang Meng went through a few more facility and then you and Shang Meng went home as the sky turns dark."

        scene home with dissolve
        show mainchar at left with dissolve
        mainchar "You sure you don't want to see the fireworks?"
        show meng at right with dissolve
        meng "If we stay there for the firework, then we will have a hard time leaving there."
        meng "There will be a huge traffic there when the firework ends."
        meng "Since you are not interested and you seem tired, I don't think it is worth the trouble."
        mainchar "But I thought you like the fireworks?"
        meng "There will always be a chance to see the fireworks."
        mainchar "That's very nice of you~"
        meng "Stop making fun of me...... Speaking of which, you told me in the morning that you need to make the decision of taking which offer, don't you remember?"
        mainchar "Oh right, it's almost next week... I need to make a respond to those offers."
        stop music fadeout 1.0
        menu:
            "Graduation School" if occupation ==0 or occupation == 1:
                mainchar "I think I will continue to the graduation school."
                mainchar "It was my dream to have a PHD degree, let's keep it that way."
                meng "I'm so glad, that you can continue on chasing your dream~"
                meng "We should celebrate this moment, no?"
                jump grad
            "Job Offer from Chen" if occupation == 0 or occupation == 3:
                mainchar "I think I will take the Job Offer from Mr.Chen."
                mainchar "He seem to be very interested with my speech on the graduation ceremony."
                meng "Was he the one who talked to you at the theme parK? I saw you guys talking and think it might be something important so I did not show up."
                mainchar "Yes, he was asking if I was going the accept it."
                meng "Sounds nice, lets go to the theme park again for the celebration! I want to see the firework show this time~"
                mainchar "......Sure."
                jump job
            "Join Eileen's Company" if occupation == 0 or occupation == 2:
                mainchar "I think I will join the start up company that Eileen started."
                mainchar "He said that I could even be one of the founders."
                meng "That was a path I did not expect...... But wow you are starting a business with Eileen."
                meng "The one who you find to be very good with computer science?"
                mainchar "Yeah, though the majority of my job is to train the model and he will be handeling the rest......"
                meng "Sounds like you are going to be very busy in the next couple of years."
                meng "Thus in order to be well prepared for that, let's go do some celebration shall we?"
                jump startup
            "Reject all of the offers" if occupation == 0:
                mainchar "I just don't feel like any of those."
                mainchar "Life is long, long enough for me to find something I want to do."
                mainchar "Life is also short, too short that I can't waste my time on something I don't want to do."
                meng "There you go, we should have a party to celebrate this~"
                jump endalone

    label grad:
        scene campusway
        n"It has been serveral years after you have made the decision."
        n"With the help Dr. Kalifer provided and your effort, you sucessfully finished your master degree and you are ready to continue for a PHD."
        n"To achieve the goal that has been a dream for the past twenty years."
        n"But meanwhile, through the time you have also heard many words that are saying it might not be a good idea to gain a PHD degree."
        n"Words including 'overqualified', 'no actual job experience', 'almost 30 years old but don't have reliable income'."
        n"You have questioned yourself as well."
        n"'Was all these really worth it?'"
        n"'My other friends who only have master degree or bachelor degree are already working and have a good salary...'"
        n"'Will I be able to get similar or higher salary?'"
        n"'If I can't what is the point of all these effort?'"
        n"'Was my dream just a immatrue ambition and I have made the wrong decision?'"
        n"With huge pressure and self-doubt, you felt exhausted."
        n"And those caused you to be even more nervous with thesis defense. Unfortunately you made a few mistakes and you are worried if you could pass the defense."
        n"All the pressure merge into a huge strength, makes you having a hard time to breathe."
        n"The exhaustion and frustration makes you felt so tired and wish to talk to someone to share your worries."
        n"Who will you choose?"
        menu:
            "Dr. Kalifer":

                jump endkalifer

            "Shang Meng" if sDream == 10:

                jump trueend

    label job:
        #项目犯错
        scene roof with fade
        n"It has been serveral years after you have made the decision."
        n"You are involved with many projects and you did well with your part."
        n"But in a recent project that was very important, you made a mistake that causes the delay of the project's deployment."
        n"Though you did your best to fix the problem and you were significant to make sure that the project's deployment was not that late."
        n"And the actual result after the deployment seems good as expected on the origional deployment date, you still felt guilty with that."
        n"On the other hand, it was the important period that if you did well there is a high chance of getting promoted."
        n"But after such mistake, it feels like the promotion will not happen anymore."
        n"Thus you want to find someone to talk about your trouble."
        n"Who will you choose?"
        menu:
            "jump endchen":

                jump endkalifer

            "Shang Meng" if sDream == 10:

                jump trueend

    label startup:
        #首次发布反向不好，怀疑是否是自己训练的不好
        scene roof with fade
        n"It has been couple years after you have made the decision."
        n"Thanks to all the efforts that Eileen , the team and you have made."
        n"The trainning of the model seem sucessful and has passed all the tests."
        n"But unfortunatly, the initial deployment of the product does not give a very good market feedback."
        n"As you seen Eileen was struggling to figure out the reason of the problem, you felt that it might be your problem that causes the user experience not very satisfactory."
        n"Though Eileen is still very possitive and encouraging everyone to the next round of development with patience and passion."
        n"But you can still sometimes see the tiredness in his eyes. Yet there are nothing you can do to help him."
        n"You felt so bad for this situation thus you could really need someone to talk to......"
        n"Who will you choose?"
        menu:
            "Eileen":

                jump endeileen

            "Shang Meng" if sDream == 10:

                jump trueend


# ending

    label endalone:
        scene roof with fade
        play music "audio/morning.mp3" fadeout 1.0 fadein 3.0 loop
        n "It has been a few years after you have made the decision."
        n "You moved to another city to seek for posibilities."
        n "And loose contact with some of the friends that was close to you."
        n "Thus sometimes you would look at the old pictured you had, to maintain the memory with them."
        n "Now you have a normal job, but you still haven't give up on finding what you really want to do."
        n "You are still full of passion, believe that one day..."
        n "You will be able to find the goal of your life and chase for it."
        scene alone with fade
        n"Although you still don't have much idea of where to go."
        n"But you belived that all you need is just an opportunity."
        n"Thus you always maintain a good mindset, in order to prepare and wait for the opportunity to come."
        n"You are sure that if the opportunity comes, you will have a very high chance to grab it and hold it in your hand tightly."
        mainchar"Life is a long advanture to explore."
        mainchar"One day I will all find my goal, and race to our destination."
        mainchar"Just like these meteors, when they are attracted by the gravity of the earth from the outer space......"
        mainchar"They have found the destination they are going to reach."
        mainchar"I am never alone, I'm......"
        mainchar"...I'm along with the stars."
        n"End No.5: Along with the stars"
        $ renpy.movie_cutscene("images/credits.webm",stop_music=False)
        scene black
        n "Click the screen to return to the main menu."
        return

    label endchen:
        scene officec with fade
        show mainchar at left with dissolve
        n "It wasn't hard at all to find Mr. Chen while work time."
        n "After a knock on the door, he let you into his office."
        show chen at right with dissolve
        n "He quickly finishes his phone call while you enter, with a cup of wine in his hand."
        chen "[povname]? Didn't expect to see you at this moment...... Are there anything you want to talk about?"
        mainchar "Mr. Chen, I still can't get rid of that thought..."
        mainchar "If I didn't made the mistake....."
        mainchar "Will we be able to make the project even more sucessful?"
        chen "My friend, seem like that little mistake you made really bothers you."
        chen "Well, as we just finished the deployment there are not much we need to do, let's talk about it."
        chen "Follow me."
        n"He stood up, led me to the elevator and we went outside of the company, the view of the far buildings was all in one view."
        scene endc with fade
        play music "audio/space.mp3" fadeout 1.0 fadein 3.0 loop
        chen "In the past twenty-ish years, I have learnd a lesson."
        chen "What's happend is happened."
        chen "Don't let them stop you from being someone you want to be my friend."
        chen "It's not an excuse to do nothing."
        chen "You need to move on."
        chen "We all made mistakes before."
        chen "The key is to learn from the past."
        chen "And carry on."
        chen "The first step is to accept yourself."
        chen "Accept your weakness."
        chen "Accept your failure."
        chen "Accept your situation."
        chen "Then you can grow from that."
        chen "See those tall buildings back there?"
        chen "Years ago when I just got into this company, those building were just starts their construction."
        chen "Every business that is big, starts from something small."
        chen "You will not achieve sucess in one day."
        chen "That is why it's worth it to chase it with the best you could do."
        chen "Keep growing, then one day you will become who you actually want to be."
        chen "And remember......"
        chen "...Whenever you felt confused, or you felt you are lost."
        chen "Look at what you have acomplished."
        chen "The progress you have made will never lie."
        chen "You did well."
        chen "Cheers."
        n"End No.4: Progress Never lie"
        $ renpy.movie_cutscene("images/credits.webm",stop_music=False)
        scene black
        n "Click the screen to return to the main menu."
        return

    label endkalifer:
        n"You decide to talk to Dr.Kalifer about your worries."
        n"Fortunately, you find Dr.Kalifer while he was taking a lunch walk."
        show mainchar at left with dissolve
        show kalifer at right with dissolve
        kalifer "Hi, [povname]. How's it going?"
        mainchar "Hi Dr. Kalifer. Not too bad, I just want to talk about the thesis defense......"
        kalifer "What about it? I heard that you made some mistakes but I think it should not be a big problem."
        mainchar "Not only that...... I was not only worrying about the defense, but also my future after graduation......"
        mainchar "I heard many words of people talking about how useless a PHD degree is."
        mainchar "And all of my friends who did not continue to graduate school seem to have their life on track."
        mainchar "Some of them even got married..."
        mainchar "I just felt confused... What is all these for?"
        n"Suddenly, Dr. Kalifer pats your shoulder. You felt a kindly sight falls on you."
        kalifer "Glad you asked, you were not the first one who have this question."
        kalifer "Come, I will show you something."
        n "He led you to his office, its a large room with a huge while board at the back."
        n "When you walkin, he picked up a piece of document in his hand and turned the projector on......"
        scene endk with fade
        play music "audio/noreturn.mp3" fadeout 1.0 fadein 3.0 loop
        kalifer "I used to have the same question."
        kalifer "But I am not going to tell you what you should do."
        kalifer "I will tell you what is the answer I found."
        kalifer "But I want you to find your own answer to the question."
        kalifer "Just like what you always do."
        kalifer "Many people believe that life is a track for race."
        kalifer "Everyone only cares about the speed of them."
        kalifer "Like there is a established path for everyone already."
        kalifer "Graduate from university, get a job, then get married. After that have children, then retire after gets to the elder ages."
        kalifer "But there was never a established path for anyone. Not for me, not for you."
        kalifer "No one can limit your life, except yourself."
        kalifer "As a scholar, I have find my path as a trailblazer."
        kalifer "This is one of the researches I did before."
        kalifer "You probablly have read some of my researches already."
        kalifer "Explore in my area of study, do reasearch and be the trailblazer in this field for the human civilization is my answer."
        kalifer "There are no established paths beyond the edge of all the known knowledge of our civilization."
        kalifer "Thus it is meaningful to explore, to make a contribustion and leave the proof of my existence."
        kalifer "The so-called trailblazing is to go further along the unfinished path of predecessors."
        kalifer "I am not saying that this must be your path as well, being someone like me."
        kalifer "But be brave to step into the field that you don't know what might be there."
        kalifer "You might felt alone, you might felt you can't see what is beyond in the path named life."
        kalifer "There are a lot of things you could do."
        kalifer "Ignore the words came out of nowhere."
        kalifer "Think outside of the box."
        kalifer "Find your own way to continue your journey."
        kalifer "And trust the decision you have made."
        kalifer "This, is the meaning of trailblaze."
        kalifer "Be the trailblazer of your own life."
        n"End No.3: The meaning of Trailblaze"
        $ renpy.movie_cutscene("images/credits.webm",stop_music=False)
        scene black
        n "Click the screen to return to the main menu."
        return

    label endeileen: 
        scene officee with fade
        n"Though Eileen is very busy and tired, but you believe that you need to talk to him."
        n"To ask if there are anything you could do to help him."
        n"Even it only means a few hours of rest for him."
        n"As you felt this is your responsibility as one of the founders."
        show eileen at right with dissolve
        show mainchar at left with dissolve
        n"It was not hard to find Eileen, he was sleeping in his office in the company. As the whole tech department and the production department are working overnight."
        mainchar"Are you still asleep?"
        eileen"......What time is it?"
        mainchar"Eleven in the morning."
        eileen"When did you sleep?"
        mainchar"I didn't, what about you?"
        eileen"Does not matter. What's up?"
        mainchar"We need to talk."
        eileen"Sure, plenty of time left until lunch. We surely can chat for a bit."
        mainchar"I probablly don't have to state our situation again but...... what are we actually doing? I want to help, not just as a developer but as one of the founders."
        play music "audio/newjourney.mp3" fadeout 1.0 fadein 3.0 loop
        eileen"You want to know the actual answer?"
        mainchar"......"
        eileen"I don't know."
        eileen"Let me show you something."
        n"Eileen grabs his smaller backpack and steped out of the office with you."
        n"After taking the elevator for a minute, you got to the roof top of the building."
        n"He steped to the side of the fense, behind him is a great view of the city."
        scene ende with fade
        eileen"If you ask, I have no idea what is wrong and what we can do."
        eileen"All the time I have been asking myself."
        eileen"What should I do?"
        eileen"There are no answers. No one can answer that for me as well."
        eileen"But I never wait until there is an answer."
        eileen"I would do something, instead of doing nothing."
        eileen"In most of the case, doing something is better than nothing."
        eileen"As there should never be an excuse name 'tomorrow'."
        eileen"There is no tomorrow."
        eileen"The action I took might not be the best it could in theory."
        eileen"But it is the best I could think of."
        eileen"Life is too short for hesitation."
        eileen"If we spend all the time to pick the best action we could at the moment..."
        eileen"We might miss the opportunity, and all we have left is regret."
        eileen"Act now, even if later on we might find a better option later on."
        eileen"At least we tried."
        eileen"Dream's big, make it happen."
        eileen"Will you be with me for this journey? My friend."
        eileen"You and Me, there shall be nothing that we can not conquer."
        n"End No.2: Dream's big, make it happen"
        $ renpy.movie_cutscene("images/credits.webm",stop_music=False)
        scene black
        n "Click the screen to return to the main menu."
        return

    label trueend:
        n"It wasn't hard to find Shang Meng, as you are still living in the same residence"
        n"You spoke to meng that you want to talk to her."
        n"But she said that she was busy till late night."
        n"Though every second feels like a year but night eventually comes."
        scene home with fade
        show mainchar at left with dissolve
        show meng at right with dissolve
        mainchar "Meng, I......"
        meng "What happened, [povname]? You don't seem... very fine."
        mainchar "I felt like I'm..... Lost."
        mainchar "I made such a mistake..."
        mainchar "And I can't see anything in front, at... the pathway I chose for myself."
        mainchar "Was all these effort...... a mistake?"
        mainchar "Was my decision wrong at the first place?"
        n "You felt warm in your eyes, tears are rolling around your eye socket."
        n "You are trying your best to pretend that you were not crying."
        n "Surprisingly, Shang Meng did not say anything."
        n "Instead, she turn around and walk out to the balcony after opening the floor-to-ceiling windows."
        n"Right at the moment, a source of light raises from the horizon."
        n"And a wind flew by, blew her ribbon on the hair away and her hair got blown by the wind."
        play music "audio/feathermain.mp3" fadeout 1.0 fadein 3.0 loop
        scene trueend with fade
        meng "Was that all of your trouble?"
        meng "That's not very like you."
        meng "The you I know wouldn't be like this."
        meng "You little fool."
        meng "The sufferings of the past have made us who we are today."
        meng "We might make mistakes."
        meng "We might meet challenges."
        meng "We might feel desperate."
        meng "These could make you felt that you have stepped on the wrong path."
        meng "Every path is a different journey."
        meng "We could never roll back and make a different decision."
        meng "Those path that you didn't choose could led to even darker places."
        meng "Believe in yourself for making the decision."
        meng "You were never alone."
        meng "I'm with you."
        meng "So are your friends and others who cares about you."
        meng "Don't be upset."
        meng "Don't regret."
        meng "Look ahead."
        meng "No matter how dark the nights are..."
        meng "No matter how long the nights will be..."
        meng "The Sun also rises."
        meng "Life isn't just about making the 'right' decision."
        meng "It's a long and unpredictable adventure."
        meng "You will meet many people."
        meng "And create memory with them."
        meng "Embrace the journey." 
        meng "Cherish the memories." 
        meng "And savor the very essence of being."
        meng "Let not regret shadow your steps."
        meng "Our lives was never perfect."
        meng "In the end, every path we took is part of our story..." 
        meng "...a verse in the grand poem of life."
        meng "And a path..."
        meng "...To an imperfect tomorrow."
        n "End No.1: To an imperfect tomorrow"
        $ renpy.movie_cutscene("images/credits.webm",stop_music=False)
        scene black
        n "Click the screen to return to the main menu."
        return

    return
