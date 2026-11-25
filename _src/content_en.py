from layout import BASE, PACKAGE, play_url, article_schema


def cta(where, text="Get it free on Google Play"):
    return f'<a class="cta" href="{play_url(where, "en")}" rel="noopener">{text}</a>'


def life_grid(lived, total=4160):
    cells = "".join('<i></i>' if n < lived else '<i class="f"></i>' for n in range(total))
    return (f'<div class="weeks" role="img" aria-label="Grid of an 80-year life in weeks: '
            f'{lived} weeks lived and {total - lived} still ahead">{cells}</div>')


HOME_BODY = f"""
<h1>Momentum: app blocker and Reels blocker for Android</h1>
<p class="lead">Block only Instagram Reels or YouTube Shorts, set time limits for your apps and get your focus back. It is free, has no ads and works without an account.</p>
<p>{cta("home-top-en")}</p>

<h2>What you can do with Momentum</h2>
<div class="grid">
<div class="card"><h3>Block Reels and Shorts</h3><p>Turn off just the section that hooks you, like Instagram Reels or YouTube Shorts, and keep using messages and the rest of the app.</p></div>
<div class="card"><h3>Time limits per app</h3><p>Set a daily limit for each app or social network. When you reach it, Momentum blocks it.</p></div>
<div class="card"><h3>Schedules and places</h3><p>Block by days and hours, or by place or Wi-Fi network: at school, at the office or at home.</p></div>
<div class="card"><h3>Focus mode and Pomodoro</h3><p>Focus sessions of 25/5 or your own length, with goals, streaks and grace days.</p></div>
<div class="card"><h3>Minimalist launcher</h3><p>Replace your home screen with a simple interface with phone, messages and contacts, without changing phones.</p></div>
<div class="card"><h3>My life in weeks</h3><p>See your life as a grid of weeks, with widgets and a wallpaper to remind you what matters.</p></div>
</div>

<h2>Get started in three steps</h2>
<ol>
<li><strong>Install Momentum</strong> from Google Play. You do not need to create an account.</li>
<li><strong>Choose what to block</strong>: a section such as Reels or Shorts, a whole app with a daily limit, or a schedule.</li>
<li><strong>Turn on the accessibility service</strong> when the app explains it. It lets Momentum know which app or section you have open so it can apply your rules.</li>
</ol>
<p>{cta("home-steps-en")}</p>

<h2>Guides to stop doomscrolling</h2>
<ul>
<li><a href="{BASE}/en/block-reels-shorts-android/">How to block Instagram Reels and YouTube Shorts on Android</a></li>
<li><a href="{BASE}/en/reduce-screen-time-android/">How to reduce screen time on your phone: 8 steps</a></li>
<li><a href="{BASE}/en/life-in-weeks-app/">Your life in weeks: what it is and how to see it on your phone</a></li>
</ul>

<h2>Your privacy</h2>
<p>Your blocking rules and what the accessibility service reads stay on your phone. Momentum does not store it, does not send it to any server and does not share it with third parties. You can turn the service off at any time in Settings &gt; Accessibility.</p>

<h2>Frequently asked questions</h2>
<details><summary>Is Momentum free?</summary><p>Yes. All features are available without payment and the app shows no ads.</p></details>
<details><summary>Do I need an account?</summary><p>No. You can use Momentum without creating an account.</p></details>
<details><summary>Can I block only Reels without blocking all of Instagram?</summary><p>Yes. Momentum can block just the Reels section of Instagram or YouTube Shorts and let you keep using messages and the rest of the app. It also has a communication-only mode that allows messages and blocks feeds, stories and reels.</p></details>
<details><summary>Why does it ask for the accessibility permission?</summary><p>Android only lets an app see which app or section is open through the accessibility service. Momentum uses it only to apply your rules: when one matches, it shows the block screen or returns to the home screen. The service only turns on if you accept the notice in the app and enable it in Android settings.</p></details>
<details><summary>What if I want to remove the block in a moment of temptation?</summary><p>You can protect your rules with a password and use an emergency unlock. There is also nuclear mode, the strongest block: once it is on, it cannot be turned off until the period you chose ends.</p></details>
<details><summary>Is Momentum an accessibility tool for people with disabilities?</summary><p>No. It uses Android's accessibility service only for its blocking features.</p></details>
<details><summary>Is it affiliated with Instagram, YouTube or TikTok?</summary><p>No. Momentum is independent and has no relationship with those apps.</p></details>
<p>{cta("home-bottom-en")}</p>
"""


def home():
    return dict(
        lang="en", path="/en/", home=True, alt="/",
        title="Momentum: App Blocker and Reels & Shorts Blocker for Android",
        description="Block Reels and Shorts without blocking the whole app, set time limits for your apps and cut your screen time. Free, no ads and no account needed.",
        h1="Momentum", body=HOME_BODY,
        schema=[{
            "@context": "https://schema.org", "@type": "MobileApplication",
            "name": "Momentum: App & Reels Blocker", "alternateName": "Momentum",
            "operatingSystem": "Android 8.0+", "applicationCategory": "LifestyleApplication",
            "description": "App and social media blocker for Android: block Reels and Shorts, limit screen time and use focus mode.",
            "url": BASE + "/en/", "inLanguage": ["en", "es", "pt", "de", "fr"],
            "downloadUrl": f"https://play.google.com/store/apps/details?id={PACKAGE}",
            "installUrl": f"https://play.google.com/store/apps/details?id={PACKAGE}",
            "image": BASE + "/assets/icon.png",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        }])


REELS_BODY = f"""
<h1>How to block Instagram Reels and YouTube Shorts on Android</h1>
<p class="meta">Updated November 25, 2026 · 6 minute read</p>
<p class="lead">You open Instagram "for a second" to check a message and forty minutes later you are still swiping short videos. This guide covers what you can do with the settings your phone and the apps already have, and how to block just that section with Momentum.</p>

<h2>Why short videos are so hard to quit</h2>
<p>Reels, Shorts and TikTok videos share one design: each clip lasts seconds, the next one starts by itself and there is no natural ending. Nothing on the screen tells you that you have seen enough. That is why willpower often loses to design, and why it helps to put up a barrier that does not depend on you remembering in the moment.</p>

<h2>What you can do without installing anything</h2>
<h3>On YouTube: limit or turn off Shorts</h3>
<p>YouTube added a daily timer for the Shorts feed in October 2025 and, in April 2026, began letting you set it to zero minutes, which turns off most Shorts on your phone. You find it in the app's time management setting. Where it sits and whether you have it depends on your YouTube version and account, so update the app if you do not see it. With a limit above zero, the prompt that appears when you reach it can be dismissed, so it works as a soft brake.</p>
<h3>On Instagram: there is no switch for Reels</h3>
<p>Instagram has no setting that turns Reels off. You can reduce them: switch your home feed to Following, tap "Not interested" on Reels you do not want and adjust your suggested content preferences. It helps, but Reels still show up in Explore and in messages.</p>
<h3>On Android: a limit for the whole app</h3>
<p>The app timers in Android's Digital Wellbeing limit the entire app. They work, but when time runs out they also block direct messages, which you may actually need.</p>

<h2>Block just the section with Momentum</h2>
<p>Momentum blocks the specific section (Instagram Reels, YouTube Shorts, Explore and others) and leaves the rest of the app available. It also has safeguards so you do not turn the rule off in a moment of temptation.</p>
<ol>
<li>Install Momentum from Google Play. You do not need to create an account.</li>
<li>Open <strong>Settings &gt; In-app blocking</strong>. You will see ready-made rules such as Instagram Reels, Explore, YouTube Shorts and Facebook Reels, among others.</li>
<li>Tap the notice to turn on monitoring. Momentum explains what it uses the accessibility service for and takes you to Android settings to switch it on.</li>
<li>Turn on the rules you want. The screen shows how many are active.</li>
<li>Open Instagram or YouTube. When you enter the blocked section, Momentum shows its block screen or sends you back to the home screen, and the rest of the app keeps working.</li>
</ol>
<p>{cta("guide-reels-steps-en")}</p>

<h2>Stop yourself from switching it off</h2>
<ul>
<li><strong>Password:</strong> protect your rules so that changing them requires a password.</li>
<li><strong>Communication-only mode:</strong> allows messages and blocks feeds, stories and reels.</li>
<li><strong>Schedules:</strong> block by days and hours, for example while you study or sleep.</li>
<li><strong>Nuclear mode:</strong> the strongest block. Once it is on, it cannot be removed until the period you chose ends. Use it with care.</li>
</ul>

<h2>An honest limitation</h2>
<p>Apps change their design often. If Instagram or YouTube change how a section is built, detection can fail until Momentum is updated, so keep the app up to date.</p>

<h2>Frequently asked questions</h2>
<details><summary>Does blocking Reels also block Instagram messages?</summary><p>No. The Reels rule blocks only that section. You can keep using messages and the rest of the app.</p></details>
<details><summary>Does it work with TikTok?</summary><p>Momentum includes rules for several apps, including TikTok, Facebook, Snapchat and X, as well as Instagram and YouTube. The sections available vary by app.</p></details>
<details><summary>Does Momentum read my messages?</summary><p>It does not store or send to any server what the accessibility service reads. That information is checked on your phone in the moment and is not shared with third parties.</p></details>
<details><summary>Does it cost anything?</summary><p>No. All features are free and the app has no ads.</p></details>
<p>{cta("guide-reels-bottom-en")}</p>
<p class="meta">Sources on YouTube's controls: <a href="https://support.google.com/youtube/thread/382356516/a-new-way-to-manage-your-time-on-shorts">YouTube's announcement of the Shorts timer</a> and <a href="https://www.theverge.com/streaming/912898/youtube-shorts-feed-limit-zero-minutes">The Verge on the zero-minute limit</a>.</p>
"""


def reels():
    p = dict(lang="en", path="/en/block-reels-shorts-android/", alt="/bloquear-reels-shorts-android/",
             title="How to Block Instagram Reels and YouTube Shorts on Android",
             description="Step-by-step guide to block only Reels and Shorts on Android without blocking messages: native YouTube and Instagram options and how to do it with Momentum.",
             h1="How to block Instagram Reels and YouTube Shorts on Android", body=REELS_BODY)
    p["schema"] = article_schema(p)
    return p


SCREEN_BODY = f"""
<h1>How to reduce screen time on your phone: 8 steps that work</h1>
<p class="meta">Updated November 25, 2026 · 6 minute read</p>
<p class="lead">Saying "I will use my phone less" rarely works. What works is changing your surroundings so that using it less becomes the easy option. Here are eight steps, in order, that you can apply today on Android.</p>

<h2>1. Measure how much you use each app first</h2>
<p>Before setting goals, look at the real numbers. Android has its Digital Wellbeing dashboard, and Momentum shows how long you spend in each app, your most used apps, your progress week by week and a weekly summary compared with the week before. Most people are surprised by the result.</p>

<h2>2. Pick only two or three culprit apps</h2>
<p>Trying to control everything at once is a recipe for giving up on day three. Look at your list and choose the two or three apps where time disappears without you noticing, usually one social network and one video app.</p>

<h2>3. Set a daily limit for those apps</h2>
<p>A daily limit turns "just a bit more" into a concrete decision. In Momentum you assign a time to each app or social network and, when you reach it, the app is blocked.</p>

<h2>4. Block the section, not the whole app</h2>
<p>Often the problem is not the app but one part of it: Reels, Shorts or the Explore tab. If you block the whole app you lose messages too, and that pushes you to remove the block. Blocking just the section that hooks you is easier to keep. The steps are in the <a href="{BASE}/en/block-reels-shorts-android/">guide to blocking Reels and Shorts</a>.</p>

<h2>5. Schedule hours for sleep and for work</h2>
<p>Late-night scrolling is one of the hardest habits to cut. A scheduled block, with the days and hours you choose, makes distracting apps unavailable exactly when they tempt you most: while studying, working or before bed. Momentum also supports rules by place or Wi-Fi network.</p>

<h2>6. Remove notifications you do not need</h2>
<p>Many times you pick up the phone because a notification called you. In Android settings, turn off notifications from apps that are not people: promotions, video suggestions, "we miss you". Keep messages and calls.</p>

<h2>7. Make your phone more boring</h2>
<p>Colors and icons are designed to grab attention. Two changes help: move tempting apps off your home screen and, on many phones, switch the screen to grayscale during rest hours. To go further, a minimalist launcher leaves only phone, messages and contacts.</p>

<h2>8. Replace the habit, do not just remove it</h2>
<p>If you remove scrolling and put nothing in its place, the gap fills with another app. Use that time for a focus session: Momentum has a Pomodoro timer (25/5) or your own duration, with daily and weekly goals and streaks. Check your summary every week and adjust your limits.</p>

<div class="card"><p><strong>A useful warning:</strong> if you use Momentum's strictest mode (nuclear mode), once it is on it cannot be removed until the period ends. Start with normal limits protected by a password, and keep nuclear mode for when you already know your habits.</p></div>

<p>{cta("guide-screen-bottom-en")}</p>

<h2>Frequently asked questions</h2>
<details><summary>How many hours of screen time are too many?</summary><p>There is no number that fits everyone. What helps is comparing with your own goal: how much time you would like to give each app and how much you actually give it. That is why the first step is to measure.</p></details>
<details><summary>Do I have to pay to use time limits?</summary><p>No. In Momentum the limits, schedules and the other features are available without payment.</p></details>
<details><summary>Can I keep using my messages?</summary><p>Yes. You can block only the sections that distract you or use communication-only mode, which allows messages and blocks feeds, stories and reels.</p></details>
"""


def screen():
    p = dict(lang="en", path="/en/reduce-screen-time-android/", alt="/reducir-tiempo-de-pantalla-android/",
             title="How to Reduce Screen Time on Your Phone: 8 Steps (Android)",
             description="Eight steps to cut your screen time on Android: measure it, set app limits, schedule blocks, block Reels and Shorts, try a minimalist launcher and use focus mode.",
             h1="How to reduce screen time on your phone: 8 steps that work", body=SCREEN_BODY)
    p["schema"] = article_schema(p)
    return p


LIFE_BODY = f"""
<h1>Your life in weeks: what it is and how to see it on your phone</h1>
<p class="meta">Updated November 25, 2026 · 4 minute read</p>
<p class="lead">An 80-year life fits in a grid of 4,160 little squares. Each one is a week. Seeing all of them on a single screen changes how you think about time.</p>

<h2>Where the idea comes from</h2>
<p>The visualization became popular through the article "Your Life in Weeks", which writer Tim Urban published in 2014 on <a href="https://waitbutwhy.com/2014/05/life-weeks.html">Wait But Why</a>. Urban draws a 90-year life (4,680 weeks) as a grid where each row is a year, and asks whether you are making the most of your weeks. The idea connects to a much older tradition, <em>memento mori</em>: remembering that time is finite so you can decide better how to use it.</p>

<h2>How it is calculated</h2>
<p>A year has 52 weeks, so 80 years is 80 × 52 = 4,160 weeks. Here is an example for a 25-year-old: weeks lived are in color and the ones ahead are gray.</p>
{life_grid(25 * 52)}
<p class="meta">Example illustration: 1,300 weeks lived out of 4,160. It is not a prediction for anyone; life expectancy differs from person to person.</p>

<h2>What it is good for</h2>
<ul>
<li><strong>Perspective.</strong> Seeing the total helps separate the urgent from the important.</li>
<li><strong>Planning by weeks.</strong> A week is a more manageable unit than a year for starting a habit.</li>
<li><strong>Less wasted time.</strong> Thinking in weeks instead of minutes makes the cost of an hour of scrolling more visible.</li>
</ul>

<h2>See it on your phone with Momentum</h2>
<p>Momentum has a section called "My life in weeks":</p>
<ol>
<li>Enter your date of birth. The app works out your weeks lived and the ones left, based on a life expectancy that you can adjust.</li>
<li>Pick the colors for lived weeks, future weeks and the background.</li>
<li>Add the widget to your home screen: long-press the screen, choose "Widgets" and look for "My life in weeks".</li>
<li>If you prefer, save the grid as an image or set it as your wallpaper.</li>
</ol>
<p>There are also widgets for year progress and motivational quotes.</p>
<p>{cta("guide-life-weeks-en")}</p>

<h2>Frequently asked questions</h2>
<details><summary>Why 4,160 squares?</summary><p>Because Momentum starts from 80 years of life: 80 times 52 weeks. You can adjust the life expectancy in the app so it fits your own circumstances better.</p></details>
<details><summary>Is it a prediction of how long I will live?</summary><p>No. It is a way to visualize time, not a forecast. No grid can tell you how long you will live.</p></details>
<details><summary>Do I need an account?</summary><p>Not to use Momentum. The app asks for your date of birth to draw your grid.</p></details>
"""


def life():
    p = dict(lang="en", path="/en/life-in-weeks-app/", alt="/vida-en-semanas/",
             title="Your Life in Weeks: What It Is and How to See It on Your Phone",
             description="What the life-in-weeks visualization is (4,160 squares), where Tim Urban's idea comes from and how to see yours with a widget and wallpaper on Android.",
             h1="Your life in weeks: what it is and how to see it on your phone", body=LIFE_BODY)
    p["schema"] = article_schema(p)
    return p
