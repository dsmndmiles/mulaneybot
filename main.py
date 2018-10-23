import discord
import os
import random

from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('The horse is in the hospital')
@client.event
async def on_message(message):
   # we do not want the bot to reply to itself
    if message.author == client.user:
        return
  #hello command
    if message.content.startswith('*hello'):
        await client.send_message(message.channel, 'Hello, {0.author.mention}'.format(message))
    if message.content.startswith('Hey John'):
        await client.send_message(message.channel, 'Hello, {0.author.mention}'.format(message))
    if message.content.startswith('*commands'):
      await client.send_message(message.channel, '`My Current Commands`\n'
     'My trigger is *\n'
     '**\*hello or Hey John**: Triggers me to greet you.\n'
     '**\*commands**: Lists my commands\n'
     '**\*owo**: OwO or UwU - see what you get.\n'
     '`Keywords I Respond To`\n'
     '**midget** anywhere in your message.\n'
     '**Whiskey or Perfume?**\n'
     '**Tell me a story.**\n'
     '**street smarts** anywhere in your message.\n'
     '**Ask about my wife!**\n'
     '**Ask me how I\'m doing.**\n'
     '**John this is so sad-**')
    if message.content.startswith('Whiskey or perfume?'):
      list = ('It\'s whiskey.', 'It\'s perfume.')
      await client.send_message(message.channel, (random.choice(list)))
    if ('midget') in message.content:
      await client.send_message(message.channel, 'How dare you say midget? It\'s just as bad as the N-word!')
    if message.content.startswith('Tell me a story.'):
      list = ('I was like 12 years old and my dad walked up to me and he said, “Hello. Hello, I’m Chip Mulaney, your father.” And he said the following: “You know Leonard Bernstein was one of the great composers and conductors of the 20th century, but sometimes, he would be gay. And according to a biography I read of him, when he was holding back the gay part, he did some of his best work.” Now, we don’t have time to unpack all of that. I don’t know if he was discouraging me from being gay or encouraging me to be a classical composer, but that is how he thought to phrase it to a 12-year-old boy. How would that ever work? Like, years later, I’d be in college, about to go down on some rockin’ twink and I’d be like, “Wait a second. What would Leonard Bernstein do?”', 'I am now gross. I am damp all the time. I am damp now and I will be damp later. Like the back of a dolphin, my back. The butt part of my pants is damp a lot. I don’t think it’s anything serious, but isn’t it, though? I’ll be in a restaurant and I’ll get up and be like, “What did I sit in?” And it was me.', 'Last November, the strangest thing happened. Now, I don’t know if you’ve been following the news, but I’ve been keeping my ears open and it seems like everyone everywhere is super mad about everything all the time. I try to stay optimistic, even though I must admit, things are getting pretty sticky. Here’s how I try to look at it and it’s just me. This guy being the president, it’s like there’s a horse loose in a hospital. It’s like there’s a horse loose in a hospital. I think eventually everything’s gonna be okay, but I have no idea what’s gonna happen next. And neither do you. And neither do your parents, because there’s a horse loose in the hospital. It’s never happened before. No one knows what the horse is gonna do next, least of all the horse. He’s never been in a hospital before. He’s just as confused as you are. There’s no experts. They try to find experts on the news. “We’re joined by a man who just saw a bird in the airport.” It’s like, get out of here with that shit. We’ve all seen a bird in the airport. This is a horse … loose in a hospital.', 'My dad is so weird. I’d love to meet him someday. You know, my friend was telling me that his dad used to beat him with a belt and that’s just the setup to my story, so… Forget about that poor son of a bitch. Anyway… He was talking and I was waiting for him to be done so I could talk. So he’s “talk, talk, talk.” It’s my turn next! And… [audience laughing] I said, “My dad never hit us.” My dad is a lawyer and he was a debate team champion. So he would pick us apart psychologically. One time I was at the dinner table when I was like six, because I had to be. My dad goes, “How was school today?” I said, “It was good but someone pushed Tyler off the seesaw.” “And where were you?” “I was over on the bench.” “And what did you do?” “Nothing. I was over on the bench.” “But you saw what happened?” “Yeah, ’cause I was over on the bench.” “So you saw what happened and you did nothing?” “Yeah, ’cause I was sitting over on the bench.” “Let me ask you this. In Nazi Germany…when people saw what the Nazis were doing and did nothing, were those good people?” “No, those are bad people. You gotta stop the Nazis.” “But you saw what they were doing to Tyler and you did nothing!” “Because I was over on the bench.” And then my dad said, “Just explain to me this. How are you better than a Nazi?” And then my mom said, “I made a salad with Craisins!” And the conversation ended.')
      await client.send_message(message.channel, (random.choice(list)))
    if ('street smarts') in message.content:
      list = ('Okay, tip number one. Street Smarts! Let’s say a guy pulls a knife on you to mug you.” You know how a mugger thinks. “Man, I need cash for drugs right now. Hey, maybe that eight-year-old with the goddamn Aladdin wallet that only has blank photo laminate pages in it will be able to help.” Let’s say a guy pulls a knife on you to mug you. What do you do? You go fumbling for your wallet. And you go fumbling for your wallet. Well, in that split-second,that’s when he’s going to stab you. So here’s what you do. You kids get yourselves a money clip. Okay, you can get these at any haberdashery. You put a $50 bill in the money clip then when a guy flashes a blade, you go, ‘You want my money, go get it!’ Then you run the other direction.', 'Tip number two. Street Smarts! Let’s say a kidnapper throws you in the back of a trunk…Let’s say a kidnapper throws you in the back of a trunk. Don’t panic. Once you get your bearings… find the carpet that covers the taillight, peel back the carpet, make a fist, punch the taillight out the back of the car, thus creating a hole in the back of the automobile, then stick your little hand out and wave to oncoming motorists to let them know that something hinky is going on.', 'Tip number three. Street Smarts! You kids have no upper body strength. If some guy tries to grab you, you can’t fight him with fists. So here’s what you do. You kids fall down on your back and you kick upward at him. That’ll throw him off his rhythm He’s not gonna know how to fight back with two little sneakers coming at him. If the Lindbergh baby had steel-toe boots, he’d still be alive today. Street Smarts!', 'Okay, so when you get kidnapped, the place where the guy grabs ya, in the biz we call that the primary location. Okay. Your odds of coming back alive from the primary location, about 60%. But if you are taken to a secondary location, your odds of coming back alive are slim to none. I am 35 years old and I am still terrified of secondary locations.')
      await client.send_message(message.channel, (random.choice(list)))
    if message.content.startswith('*owo'):
      list = ('OwO', 'UwU')
      await client.send_message(message.channel, (random.choice(list)))
    if message.content.startswith('John this is so sad'):
      await client.send_message(message.channel, 'Play \"What\'s New Pussycat\" seven times? https://www.youtube.com/watch?v=gWaz7Hnd1Hw')
    if ('How are you John?') in message.content:
      list = ('I\'m trying my best.', 'Life is a fucking nightmare!', 'You could pour hot soup in my lap and I\'d probably apologize to you.', 'I am homeless, I am gay, I have AIDS, and I\'m *new in town*.')
      await client.send_message(message.channel, (random.choice(list)))
    if message.content.startswith('How is your wife?'):
      await client.send_message(message.channel, 'My wife is a bitch and I *love her*.')
    
keep_alive()
token = os.environ.get("token")
client.run(token)
