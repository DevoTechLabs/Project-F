init python:
    gallery = Gallery()

    gallery.button("campusway")
    gallery.unlock_image("campusway")

    gallery.button("cafe")
    gallery.unlock_image("cafe")
    
    gallery.button("ehouse")
    gallery.unlock_image("ehouse")

    gallery.button("home")
    gallery.unlock_image("home")

    gallery.button("officec")
    gallery.unlock_image("officec")

    gallery.button("officee")
    gallery.unlock_image("officee")

    gallery.button("park")
    gallery.unlock_image("park")

    gallery.button("park2")
    gallery.unlock_image("park2")

    gallery.button("train")
    gallery.unlock_image("train")

    gallery.button("roof")
    gallery.unlock_image("roof")

    gallery.button("trueend")
    gallery.unlock_image("trueend")

    gallery.button("alone")
    gallery.unlock_image("alone")

    gallery.button("ende")
    gallery.unlock_image("ende")

    gallery.button("endk")
    gallery.unlock_image("endk")

    gallery.button("endc")
    gallery.unlock_image("endc")

screen memory:
    tag menu
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        grid 5 3:
            add gallery.make_button(name="campusway", unlocked=im.Scale("images/campusway.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="cafe", unlocked=im.Scale("images/cafe.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="ehouse", unlocked=im.Scale("images/ehouse.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="home", unlocked=im.Scale("images/home.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="officec", unlocked=im.Scale("images/officec.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="officee", unlocked=im.Scale("images/officee.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="park", unlocked=im.Scale("images/park.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="park2", unlocked=im.Scale("images/park2.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="train", unlocked=im.Scale("images/train.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="roof", unlocked=im.Scale("images/roof.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="trueend", unlocked=im.Scale("images/trueend.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="alone", unlocked=im.Scale("images/alone.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="ende", unlocked=im.Scale("images/ende.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="endk", unlocked=im.Scale("images/endk.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            add gallery.make_button(name="endc", unlocked=im.Scale("images/endc.png", 320, 180), locked=im.Scale("images/locked.png", 320, 180))
            spacing 15

        textbutton "Return" action Return()