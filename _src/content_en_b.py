from layout import BASE, article_schema
from content_en import cta


def faq(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)


def mk(path, alt, title, description, h1, body):
    p = dict(lang="en", path=path, alt=alt, title=title, description=description, h1=h1, body=body)
    p["schema"] = article_schema(p)
    return p


CHOOSE = f"""
<h1>How to choose an app blocker for Android (and what to avoid)</h1>
<p class="meta">Updated November 25, 2026 · 6 minute read</p>
<p class="lead">Google Play has dozens of apps that block apps and cut screen time. Almost all of them promise the same thing, but they do different things. This guide gives you a checklist to pick the one that solves your problem and to avoid the ones that ask for more than they need.</p>

<h2>First, define what you want to fix</h2>
<ul>
<li><strong>You spend too much time overall.</strong> You need daily limits per app and stats.</li>
<li><strong>One section hooks you</strong> (Reels, Shorts, Explore). You need section blocking, not just app blocking.</li>
<li><strong>You get distracted at certain times</strong> (studying, working, sleeping). You need schedules, or rules by place and Wi-Fi.</li>
<li><strong>You remove the block every time you are tempted.</strong> You need protection that is hard to switch off.</li>
</ul>

<h2>A checklist to compare apps</h2>
<table>
<tr><th>Criterion</th><th>What to check</th></tr>
<tr><td>Per-app limits</td><td>Can you set a different daily time for each app?</td></tr>
<tr><td>Section blocking</td><td>Does it block just Reels or Shorts, or does it force you to block the whole app?</td></tr>
<tr><td>Schedules and places</td><td>Can you pick days and hours, or rules by place or Wi-Fi network?</td></tr>
<tr><td>Protection</td><td>Is there a password, an emergency unlock or a mode that is deliberately hard to turn off?</td></tr>
<tr><td>Price and ads</td><td>Which features are behind a payment? Does it show ads, which work against the goal of being less distracted?</td></tr>
<tr><td>Account</td><td>Can you use it without creating an account? The less data you hand over, the better.</td></tr>
<tr><td>Privacy</td><td>What does it read, where is it processed and is it sent to a server? Check the Google Play listing and its privacy policy.</td></tr>
<tr><td>Maintenance</td><td>Was it updated recently? Section-blocking apps depend on keeping up with changes in Instagram and YouTube.</td></tr>
</table>

<h2>Permissions: what is normal and what is not</h2>
<p>To work, a blocker needs to know which app you have open. Android allows that through permissions such as usage access, drawing over other apps or the accessibility service, which can also recognize sections inside an app. Asking for them is normal. Asking for your contacts, SMS or location without explaining why is not. Before you accept the accessibility service, check that the app clearly explains what it uses it for and what it does with what it reads.</p>

<h2>How to test an app before committing</h2>
<ol>
<li>Install only one app at a time, so you know which one works.</li>
<li>Create a single rule for your biggest problem (for example, Reels or 30 minutes of one social network).</li>
<li>Use it for three days without changing anything and see if your screen time drops.</li>
<li>If it gets in the way more than it helps, uninstall it. You do not have to keep it.</li>
</ol>

<h2>Where Momentum fits</h2>
<p>Momentum covers the criteria in the table: time limits per app, blocking of sections such as Reels and Shorts, schedules, rules by place or Wi-Fi, password protection with an emergency unlock and a nuclear mode. It is free, has no ads and works without an account. What the accessibility service reads is checked on your phone and is not stored or sent to any server.</p>
<p>It also has limits you should know about: it is Android only, section blocking depends on Instagram, YouTube and other apps not changing how they are built, and that feature needs the accessibility permission.</p>
<p>{cta("guide-choose-app-en")}</p>

<h2>Frequently asked questions</h2>
{faq([
    ("Does a blocker work if I can just uninstall it?", "You can uninstall any app, so the value is in what makes it harder in a moment of impulse: a password, a pause before an emergency unlock, or a mode such as nuclear mode whose early exit takes a long wait."),
    ("Do I have to pay to block apps?", "Not necessarily. Some apps charge for their main features, and others, like Momentum, offer all their features for free."),
    ("Is it safe to give an app the accessibility permission?", "It is a powerful permission, so only give it to an app that explains what it uses it for and whose listing and privacy policy say what it does with the information. You can turn it off at any time in Settings &gt; Accessibility."),
])}
"""

DOOM = f"""
<h1>How to stop doomscrolling: 7 tactics that work</h1>
<p class="meta">Updated November 25, 2026 · 5 minute read</p>
<p class="lead">Doomscrolling is swiping endlessly through news or posts, often bad ones, even when it is making you feel worse. It is not a lack of character: the apps are designed so there is no stopping point. The fix is to add friction to the path.</p>

<h2>1. Notice when it happens</h2>
<p>For three days, note the moments you open the app without deciding to: on waking, in bed, in the bathroom, when bored, after an argument. There is almost always a trigger, and it is easier to change one moment than a whole habit.</p>

<h2>2. Take the app out of the way</h2>
<p>Move the app off your home screen into a folder on the last page. Each extra step is a chance to reconsider.</p>

<h2>3. Block the section that hooks you</h2>
<p>The endless scroll usually lives in one place: Reels, Shorts, Explore or "For you". If you block only that section, you keep messages and everything else. There is a step-by-step explanation in the <a href="{BASE}/en/block-reels-shorts-android/">guide to blocking Reels and Shorts</a>.</p>

<h2>4. Set a daily cap</h2>
<p>Pick a realistic time for each app, say 30 minutes, and let the app lock when you reach it. Deciding once is easier than deciding every time you open your phone.</p>

<h2>5. Protect the night</h2>
<p>Late-night doomscrolling steals sleep. Schedule a block for the hour before bed and charge your phone away from the bed, so it is not the first thing you touch on waking.</p>

<h2>6. Keep a replacement within reach</h2>
<p>If the gap stays empty, the scrolling returns. Leave a book, a notebook or headphones where the phone used to be. For work or study, a timed focus session helps you start. See the <a href="{BASE}/en/pomodoro-technique-android/">Pomodoro technique guide</a>.</p>

<h2>7. Silence what calls you</h2>
<p>Turn off notifications for news and for social suggestions. Keep only the ones from people.</p>

<div class="card"><p>If phone use keeps you from sleeping, affects your mood or constantly interferes with your work or relationships, talk to a health professional. An app can help with habits, but it does not replace that support.</p></div>

<p>{cta("guide-doomscrolling-en")}</p>

<h2>Frequently asked questions</h2>
{faq([
    ("Is it the same as phone addiction?", "Not necessarily. Doomscrolling is a specific pattern: consuming content nonstop, usually negative. It can be part of problematic phone use, but it is not a diagnosis."),
    ("Is blocking the whole app better?", "Sometimes, for example during sleeping hours. But if you need the app for something else, it is more sustainable to block only the section that hooks you."),
])}
"""

POMO = f"""
<h1>The Pomodoro technique on Android: how to use it to study or work</h1>
<p class="meta">Updated November 25, 2026 · 5 minute read</p>
<p class="lead">The Pomodoro technique splits work into short blocks with breaks. It is simple, and that is why it works: starting a 25-minute task costs less than starting "studying all afternoon".</p>

<h2>What it is</h2>
<p>Francesco Cirillo created the method in the late 1980s and named it after a tomato-shaped kitchen timer. The classic version is:</p>
<ol>
<li>Pick one task.</li>
<li>Set a <strong>25-minute</strong> timer and work only on that.</li>
<li>Take a <strong>5-minute</strong> break.</li>
<li>After four blocks, take a longer break of 15 to 30 minutes.</li>
</ol>

<h2>How to do it well</h2>
<ul>
<li><strong>One task per block.</strong> If something new comes up, write it down and keep going.</li>
<li><strong>Phone out of sight.</strong> If you use it as the timer, make it the app that helps you block distractions, not a social network.</li>
<li><strong>A break is a break.</strong> Stand up, drink water, look out the window. Do not open a social network: a 5-minute break turns into 40.</li>
<li><strong>Adjust the length.</strong> If 25 minutes feels too short or too long, change it. What matters is that it stays fixed.</li>
</ul>

<h2>Doing it with Momentum</h2>
<p>Momentum has a focus mode with a Pomodoro timer (25/5) or a duration you choose. It also includes daily and weekly goals, challenges and streaks, TimeCoins for every focused minute and grace days that protect your streak when a day gets hard.</p>
<p>So that your phone is not the source of interruptions, combine it with per-app limits and with <a href="{BASE}/en/block-reels-shorts-android/">blocking Reels and Shorts</a>.</p>
<p>{cta("guide-pomodoro-en")}</p>

<h2>Frequently asked questions</h2>
{faq([
    ("How many pomodoros a day?", "It depends on your task. Start with two or three and build up slowly. Consistency matters more than quantity."),
    ("What if I get interrupted?", "If it is brief, note it and go back. If it is long, void that block and start a new one when you can; a half block does not count."),
    ("Can I change from 25/5 to another length?", "Yes. Momentum lets you choose the length of your focus sessions."),
])}
"""

DETOX = f"""
<h1>Digital detox: a 7-day plan to start today</h1>
<p class="meta">Updated November 25, 2026 · 6 minute read</p>
<p class="lead">A digital detox does not mean throwing your phone away. It means deciding when and why you use it. This plan spreads the changes over a week so you do not give up on day two.</p>

<h2>Day 1: measure</h2>
<p>Do not change anything yet. Write down how much time you spend today overall and in your three most used apps. That number is your starting point.</p>

<h2>Day 2: silence</h2>
<p>Turn off notifications for everything that is not a person. Without alerts, the phone stops calling you.</p>

<h2>Day 3: set limits</h2>
<p>Pick two apps and give each a realistic daily limit. In Momentum you assign a time to each app or social network and it locks when you reach the cap.</p>

<h2>Day 4: block the section that hooks you</h2>
<p>Turn on the block for Reels, Shorts or Explore, whichever is yours. You can still use messages. See how in the <a href="{BASE}/en/block-reels-shorts-android/">guide to blocking Reels and Shorts</a>.</p>

<h2>Day 5: protect your sleep</h2>
<p>Schedule a night block when distracting apps are unavailable, and charge your phone outside the bed.</p>

<h2>Day 6: simplify the screen</h2>
<p>Try a minimalist launcher for a day: only phone, messages, contacts and the apps you allow. You will notice how often you reach for an icon out of reflex.</p>

<h2>Day 7: review and decide</h2>
<p>Compare with day 1. See which rules helped and which got in the way, and keep the ones that worked. The plan does not end here: it is a starting point for more intentional use.</p>

<div class="card"><p>If limits are hard to keep, protect your rules with a password. Keep nuclear mode, which locks apps for 1 to 3 months, for when you know what works for you.</p></div>

<p>{cta("guide-detox-en")}</p>

<h2>Frequently asked questions</h2>
{faq([
    ("Do I have to quit social media?", "No. The goal is to use it by decision, not by reflex. Many people keep their networks with limits and without the sections that hook them most."),
    ("How long does a digital detox last?", "It can be a day, a week or a month. To start, seven days is enough to see what changes."),
])}
"""


def pages():
    return [
        mk("/en/choose-app-blocker-android/", "/elegir-app-para-bloquear-apps-android/",
           "How to Choose an App Blocker for Android (and What to Avoid)",
           "A checklist to choose an Android app blocker: limits, section blocking, schedules, protection, privacy and permissions.",
           "How to choose an app blocker for Android (and what to avoid)", CHOOSE),
        mk("/en/stop-doomscrolling/", "/dejar-doomscrolling/",
           "How to Stop Doomscrolling: 7 Tactics That Work",
           "What doomscrolling is and seven tactics to stop it: spot your triggers, block the section that hooks you, set time limits, protect your nights and plan a replacement.",
           "How to stop doomscrolling: 7 tactics that work", DOOM),
        mk("/en/pomodoro-technique-android/", "/tecnica-pomodoro-android/",
           "Pomodoro Technique on Android: How to Use It to Study or Work",
           "What the Pomodoro technique is (25 minutes of focus, 5 of rest), how to apply it well and how to use Momentum's focus timer on Android.",
           "The Pomodoro technique on Android: how to use it to study or work", POMO),
        mk("/en/digital-detox-7-days/", "/detox-digital-7-dias/",
           "Digital Detox: a 7-Day Plan to Start Today (Android)",
           "A 7-day digital detox plan for Android: measure, silence notifications, set limits, block Reels and Shorts, protect sleep and simplify your home screen.",
           "Digital detox: a 7-day plan to start today", DETOX),
    ]
