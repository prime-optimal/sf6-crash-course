---
created: 2023-04-01 10:36 AM
updated: 2023-05-01 07:36 PM
tags: hardware, SF6-essentials, input-lag, controllers, gp2040-ce
---
When it comes to mastering Street Fighter 6, many players focus on perfecting their combos, honing their strategies, and learning the ins and outs of their favorite characters. 

While these elements are undoubtedly crucial for success, it's equally important to ensure that your gaming setup is optimized for peak performance. 
After all, even the most skilled player can be held back by a subpar setup that results in latency or an inadequate gaming experience.

In the following sections, we'll discuss various aspects of an ideal gaming setup, from choosing the right platform and monitor to optimizing your internet connection and recording your gameplay for review. 
By investing time and effort into perfecting your setup, you'll be giving yourself the best possible chance to excel in Street Fighter 6 and have a much better experience overall. 

But first, let’s discuss some key concepts.  

## Latency 
***Latency***, or ***input lag*** is the amount of time it takes for a player’s action to be registered by the game and then displayed on screen.  
This is typically measured in milliseconds (ms), but can also be measured by frames.  

Reducing latency as much as possible is important because oftentimes in fighting games, you only have a split second to react to moves.  
Therefore, if your setup has a high amount of latency, you are reducing your chances of success and also training your muscle memory with slightly incorrect timing. 

Street Fighter 6, as well as most modern era fighting games, runs at 60 frames per second (fps).  
One second is 1,000 ms, which means that each frame the game displays takes approximately 16.67 ms.  

That may not seem like much, but when you factor in our human reactions, the time it takes for the controller to register an input, the time it takes for a monitor to display the output from the console/PC, as well as the time it takes for data packets to travel across the internet to reach your opponent, you can see how these seemingly small amounts of time add up quickly. 

```ad-info
At the launch of Street Fighter V, there were approximately 7-8 frames of input lag on the PS4 version of the game.  

This meant that there were many moves that *should* have been easy to block, but weren’t.  

Eventually, uproar from the community caused Capcom to fix the issue, and eventually the input lag was reduced to approximately four frames.  

```

The main sources of input lag are: 
- your controller 
- your display 
- your console/PC

It’s up to you to understand the latency of each component of your setup, even if you can’t immediately change it right away.  

It’s beyond the scope of this book to go deep into fully optimizing your setup, but some helpful resources are:
- [inputlag.science](https://inputlag.science/)
- [Blur Busters](https://blurbusters.com/)

Now let’s dig into each component of your setup.

## Choose the Right Controller for You
The controller you choose to play with is important because it is ultimately an extension of your mind and yourself.  Without being overly dramatic, it is the equivalent of a samurai sword in the sense that it is what you rely on for every battle and is the difference between life and death. 

Each controller has different components such as the PCB and buttons.  These contribute to its feel, responsiveness, and ultimately, your effectiveness as a player.  

There are many different choices available, but the three main categories are:
- regular d-pad controllers 
- fight sticks 
- leverless/stickless 


### Regular Pad Controllers

-   Examples: PS5 DualSense, Xbox One, Xbox 360, Hori controllers
-   Pros: Familiarity for many players, widely available
-   Cons: Some may find certain motions difficult
-   Recommendation: If you're comfortable with pad controllers, stick with them.

```ad-tip
The PS5 DualSense can be overclocked from its default polling rate of 250hz (4ms) all the way up to 1,000-8,000hz.  


However, this is only possible on PC.
```

![This is a pretty good video about input lag on controllers](https://youtu.be/Wi-40_973Es)


### Fight Sticks

-   Examples: Mad Catz, Razer, Victrix, Hori sticks
-   Pros: Many pro players use them, some find certain motions easier
-   Cons: Steep learning curve for new players.  The physical distance between cardinal directions induces a small amount of latency. 
-   Recommendation: If you've been using fight sticks since childhood or are comfortable with them, continue using them.

```ad-warning
Don't be fooled by marketing.  Playing on stick will not automatically make you a better player and just because many pro players use them, doesn't mean that you need to in order to reach your potential.

```

### Leverless Controllers (Hitboxes, Mixboxes)

-   Unique design with directional buttons instead of a stick
-   Pros: More precise inputs, innovative design
-   Cons: Controversial, may be banned in some tournaments
-   Recommendation: If you're open to trying new controllers and looking for an edge, give them a try

Ultimately, you should play on whichever style of controller you feel most comfortable with.  I’ve seen countless misguided players try to switch to stick and not see the improvements in their game they were expecting, due to the learning curve. 

However, no matter which style you prefer, you should still strive to play on the controller with the least amount of input lag possible.  This may mean swapping out the PCB in favor of another one. 

This chart from [inputlag.science](https://inputlag.science) shows the controllers with the least amount of input lag, though this could change at any time.  

![[2023-04-03-07-20-26.png|Source: inputlag.science]]

Not listed is the Raspberry Pi Pico and other boards based on the RP2040 microcontroller, which supports the open source [GP2040-CE firmware](https://gp2040-ce.info/) and has a default polling rate of 1000 hz (1ms).  

![[2023-04-03-07-29-57.png|Source: gp2040-ce.info]]

I personally haven’t tested it, but if you are handy with electronics and want the best performance possible, it’s worth investigating for sure. 


## Why Your Monitor Matters in Fighting Games
### Not All Displays Are Equal
Your monitor plays a crucial role in your fighting game experience, and it's important to understand why. 
Not all displays are created equal, and while a large TV might be perfect for movies and casual gaming, they usually aren't suitable for fighting games due to latency issues. 
As a serious player, investing in a gaming monitor should be a priority.

### Time to Invest in a Gaming Monitor
Brands like Asus, BenQ, Acer, LG, and Samsung offer gaming monitors with refresh rates ranging from 120 Hz to 500 Hz, catering to different budgets. 
You can even find deals for under $100 if you're on a tight budget. 
When it comes to upgrading your gaming setup, prioritize getting a gaming monitor before spending on a new controller or GPU.


### Prioritize Upgrading Your Monitor
[TIP] A gaming monitor is not only a solid investment in yourself as a player but also versatile, as it works well with various systems, offering more value for your money. 

Prioritize upgrading your monitor to enhance your gaming experience and performance in fighting games.
-   Before you splurge on a new controller or GPU, think about upgrading your monitor first
-   Your gaming experience and performance will thank you
-   Trust us, it's a solid investment in yourself as a player
-   The best part? Gaming monitors work with various systems, giving you more bang for your buck

## Console Apologists Beware: The Savage Truth About Upgrading to PC for Street Fighter 6
The age-old battle between PC and console gaming is still ongoing, but when it comes to fighting games, the choice is clear: PC offers a superior experience. 
Street Fighter 6, for example, is available on various platforms, including PC, PS5, Xbox One, and PS4. 
The game can run on low-end PC hardware, and there's no need for an expensive high-end PC. You can build a decent gaming PC for about $200, far less than a PS5, and it offers more utility as it can be used for purposes other than gaming.

**Important: Handle these in order**
1.  Improve internet connection (use wired Ethernet if possible).
2.  Upgrade your monitor.
3.  Switch from console to PC.
4.  Change or upgrade your controller.

## Recording Gameplay
Having a PC makes it easier to record and review your gameplay, stream, and create content. Furthermore, you can use free apps like OBS, Streamlabs OBS, or StreamElements to record and stream gameplay. 
Even if streaming isn't your goal, recording your matches on a PC makes it easier to review your replays, which is crucial for improvement.

**Tip: Capture Cards for Console Players** 
If you're playing on a console like PS4, PS5, or Xbox and have access to a PC, consider getting a capture card to record your matches. 
Although there are built-in replay functions in modern fighting games, using a capture card makes it much easier and quicker to review your gameplay. 
By recording and analyzing your matches, you can identify areas for improvement and develop strategies to outsmart your opponents. 
A small investment in a capture card can go a long way in helping you become a better player and ultimately conquer the world of Street Fighter 6.
It’s still a better choice to play and record on PC, but if you’re stuck on console, at least get the capture card. 

**Warning: WiFi Woes!** 
Don't let WiFi hold you back. 
Invest in a powerline ethernet adapter to ensure a stable connection for your gaming setup. 
This handy device allows you to plug your ethernet cable into an outlet near your gaming station and connect it to your router/modem at the other end. 
For a small investment of around 40-50 bucks, you can significantly improve your connection and boost your chances of success in Street Fighter 6. 

Your gaming setup is the one aspect of your skill development that you have full control over, so invest in it to provide yourself with the best chance of success.
