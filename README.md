<h1>monkmode</h1>
<img width="50%" alt="monkmode" src="https://github.com/user-attachments/assets/b6afc1d8-68b1-42ad-b760-2690c1c40023"/>

<h2>App's Goal and Idea Behind It</h2>

<p>The ultimate goal of monkmode is to help you achieve a monk-like state of focus, allowing you to maximize deep work. It does this by breaking your overall focus goal into structured focus sessions, short breaks, and long breaks. This approach is a well-known technique used by high achievers and students alike. By working in focused bursts, you can maintain higher levels of concentration, which in turn helps you accomplish more.</p>

<p>My main motivation for creating monkmode was to build a <strong>minimalistic, useful focus app with no fluff</strong>—straight to the point. Before monkmode, I was using Windows' built-in focus features, but after encountering various bugs and limitations, I decided to create a <strong>cleaner, more reliable alternative</strong> that does exactly what you need: stay focused and track your sessions efficiently.</p>


## Download and Installation

### Windows (Recommended)
1. Go to [Releases](https://github.com/dop14/monkmode/releases)
2. Download the latest `monkmode.exe`
3. Double-click to run - no installation required!

#### Windows Security Notice
Windows Defender may show a warning when downloading or running the executable. This is normal for unsigned applications. To run the app:

1. **When downloading**: Click "Keep" if browser shows a warning
2. **When running**: Click "More info" → "Run anyway" if Windows Defender blocks it
3. **Alternative**: Right-click the .exe → Properties → Check "Unblock" → Apply

This happens because the executable isn't code-signed. The app is safe to use - you can verify by checking the source code in this repository.

### Linux
#### Option 1: Run from source
```bash
# Clone the repository
git clone https://github.com/yourusername/monkmode.git
cd monkmode

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

#### Option 2: Build your own executable
```bash
# Follow steps above, then:
pip install pyinstaller

# Linux build command
pyinstaller --onefile --windowed \
--name monkmode \
--icon=logo/monkmode.png \
--add-data "database/schema.sql:database" \
--add-data "logo/monkmode.png:logo" \
--add-data "logo/monk.png:logo" \
--add-data "monkmode_sounds/break_start.wav:monkmode_sounds" \
--add-data "monkmode_sounds/focus_start.wav:monkmode_sounds" \
main.py

# Find executable in dist/ folder

```

### macOS
#### Option 1: Run from source
```bash
# Clone the repository
git clone https://github.com/yourusername/monkmode.git
cd monkmode

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

#### Option 2: Build your own executable
```bash
# Follow steps above, then:
pip install pyinstaller

# macOS build command
pyinstaller --onefile --windowed \
--name monkmode \
--icon=logo/monkmode.png \
--add-data "database/schema.sql:database" \
--add-data "logo/monkmode.png:logo" \
--add-data "logo/monk.png:logo" \
--add-data "monkmode_sounds/break_start.wav:monkmode_sounds" \
--add-data "monkmode_sounds/focus_start.wav:monkmode_sounds" \
main.py

# Find executable in dist/ folder
```

### Requirements
- **Windows**: No requirements - executable includes everything
- **Linux/macOS**: Python 3.8+ and dependencies listed in `requirements.txt`

<h2>What Are Focus Periods</h2>

Focus periods are the core of deep work. When you first run monkmode, the default focus period is called "pomodoro", one of the most popular focus techniques: it divides work into 25-minute focus sessions followed by 5-minute breaks. After completing four focus sessions, the next break is a long break, usually around 15 minutes.

<h3>Creating a New Focus Period</h3>

<p>With monkmode, you can create custom focus periods however you like.</p>
<img width="40%" alt="monkmode_add_period" src="https://github.com/user-attachments/assets/14db76d9-5230-4128-9b70-f56ff2be2e16" />
<img width="25%" alt="monkmode_new_period" src="https://github.com/user-attachments/assets/c22f8f63-2438-4cfb-9498-4d76cdd20ad9" />

<h3>Editing an Existing Focus Period</h3>

<p>You can edit any previously created focus period, including the default "pomodoro". When you press Edit, the currently selected focus period will be modified according to your changes.</p>
<img width="40%" alt="monkmode_edit_period" src="https://github.com/user-attachments/assets/21df20a3-36fd-4fbb-bd9f-edee7839f144"/>
<img width="25%" alt="monkmode_edit_focus" src="https://github.com/user-attachments/assets/008b4da8-8ffa-4293-a209-c57fd36c9f18" />

<h3>Deleting a Focus Period</h3>

<p>You can delete any focus period except the default one. Be careful — this action cannot be undone.</p>
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/e0a9378f-08d0-4451-95ac-6bdb23000c23" />

<h2>What Are Focus Subjects</h2>

Focus subjects are the topics you will be concentrating on during your focus sessions.
<p><i>Note: The interface for adding, editing, deleting focus subjects works the same as for focus periods (see screenshots above).</i></p>
<h3>Creating a New Focus Subject</h3>

When creating a new focus subject, you can be as detailed as you like. The only required parameter is the name of the topic you want to focus on.

<h3>Editing an Existing Focus Subject</h3>

To edit a focus subject, first select it from the combobox. When you press Edit, the currently selected focus subject — including the default subject if chosen — will be modified according to your changes.

<h3>Archiving a Focus Subject</h3>

<p>Archiving is useful for topics you’ve finished (for example, a task, a completed university class or a side project). Archiving sets the subject aside without deleting it, so it still appears in your statistics menu.</p>

<img width="40%" alt="monkmode_archive_subject" src="https://github.com/user-attachments/assets/fb8d82dd-341f-4589-a799-4cac6b1fd084" />

<h3>Deleting a Focus Subject</h3>

You can delete any focus subject except the default one. Be careful — this action cannot be undone, and any progress linked to that subject will be lost.

<h2>How Focus Works</h2>

Starting a focus session is simple. 
<p>First, select the focus period you want to use and the subject you’ll focus on.</p>
<p>Next, press “Focus” and choose the number of focus sessions you want to complete.</p>
<img width="40%" alt="monkmode_focus" src="https://github.com/user-attachments/assets/69c92346-3c6c-4e08-a413-8a4d958996fe" />
<p></p>You’ll see the total duration of your focus time along with a breakdown of the sessions.</p>
<p>Finally, press “start focus” to begin the timer.</p>
<img width="25%" alt="monkmode_start_focus_2" src="https://github.com/user-attachments/assets/a17b1dbb-1916-4699-a298-bf93b3a6a594" />

<h2>While in Focus</h2>

Each time a focus session or a break begins, you’ll hear a distinct sound signaling the start of that session. A small pop-up text in the bottom-right corner will also appear to let you know whether a focus or break session is starting. Both the sound and pop-up notifications can be turned off in the settings menu.

<h3>Pause, Resume, and Stop</h3>

While you’re in focus, you can always pause or stop the timer:

- Pause freezes the countdown until you press Resume.

- <p>Stop ends the focus session entirely (after confirmation). Don’t worry — any progress you’ve already made will still be saved.</p>
<img width="40%" alt="monkmode_in_focus" src="https://github.com/user-attachments/assets/ec171e4f-3569-4196-9fda-8ea789a73126" />

<h3>Small View</h3>

In the top-right corner, you’ll find an icon that opens a small view of monkmode. This view allows you to track your progress while working on other tasks. The pause, resume, and stop functions work exactly as described above.

<p>You can always switch back to the fullscreen view at any time. If you find the countdown distracting, you can click on the timer to conceal the remaining time.</p>
<img width="250" height="270" alt="monkmode_small_view" src="https://github.com/user-attachments/assets/291ed080-3828-4871-863f-4a43d4714a5a" />
<img width="250" height="270" alt="monkmode_small_view_hidden" src="https://github.com/user-attachments/assets/39fafbbb-d49a-4715-9fcb-9a7e1e844a2c" />

<h2>Daily Focus Goal</h2>

<p>Your daily focus goal is the amount of time you want to spend in focused work each day. The minimum goal is 1 hour.
You can adjust your daily focus goal in the settings menu.
By completing your daily goal, you’ll earn streaks — a familiar concept for many productivity apps.</p>

<img width="40%" alt="monkmode_daily_focus" src="https://github.com/user-attachments/assets/978ca4f7-ab20-40a8-b1af-e218a77bdeb8" />

<h2>Action Bar</h2>

<p>The action bar is located in the top-left corner of the app and provides quick access to key options.</p>
<img width="40%" alt="monkmode_actionbar" src="https://github.com/user-attachments/assets/93d316d6-4ab9-4de5-a1bb-ce8b54da9260" />

<h3>Settings</h3>
In the settings menu, you can:
<ul>
   <li>Change default values</li>
   <li>Choose to show or hide the daily quote</li>
   <li>Turn focus notifications on or off</li>
   <li>Choose from 6 different themes</li>
</ul>
<p><i>Note: Changing your daily focus goal after completing it will not affect that day’s completion status.</i></p>
The default focus period and subject are automatically selected when you launch the app.</p>

<h3>Archive</h3>

The archive is where all of your archived subjects are stored. From here, you can also unarchive them at any time.

<h3>Help</h3>
The help menu contains two options:
<ul>
   <li>About → provides basic information about the app, the developer, credits, and the license used.</li>
   <li>How to Use → links directly to this README.md file (the guide you’re reading now).</li>
</ul>

<h2>Statistics</h2>
<p>
  On the main page, you can see your current week’s focus time  and your
  current streak. Press “Show All” to access more detailed statistics.
</p>
<img width="40%" alt="monkmode_stats" src="https://github.com/user-attachments/assets/d8dd3d85-2305-458b-890d-0d6838e7e37a" />

<h3>Focus statistics</h3>
<p>These statistics give you a clear overview of your progress.</p>
<p><i>Note: Focus sessions completed</strong> only count if you finish the entire session (sessions you stop early do not count).</i></p>

<h3>Streak &amp; Karma statistics</h3>
<ul>
  <li>Daily goal achieved — shows how many times you’ve completed your daily focus goal.</li>
  <li>
    Current streak — shows your ongoing streak.
    <ul>
      <li><em>Weekdays</em>: streaks are strict — if you miss your daily goal on a weekday, your streak resets to 0.</li>
      <li><em>Weekends</em>: optional — if you complete your daily goal, your streak increases; if you don’t, your streak will not reset.</li>
    </ul>
  </li>
  <li><strong>Longest streak</strong> — your all-time longest streak.</li>
  <li>
    <strong>Karma</strong> — a metric showing your consistency over the past 2 months.
    <p><strong>Formula:</strong></p>
    <pre><code>karma = (completed_days / relevant_days) * 100</code></pre>
    <p>
      <em>completed_days</em> = number of days you completed your daily goal.<br>
      <em>relevant_days</em> = all weekdays in the past 2 months + weekend days where you completed your daily goal.
    </p>
  </li>
  <li><strong>Karma levels</strong> — reflect your “monk status” in your focus journey. There are 7 levels to discover.</li>
</ul>
<img width="40%" alt="monkmode_statistics" src="https://github.com/user-attachments/assets/ea508745-eb17-49bc-b4c0-dc6dbd5c807b" />

<h3>Charts</h3>
<p>After completing at least one focus session, 5 charts will appear in the statistics window:</p>
<ol>
  <li><strong>Line chart</strong> — shows your daily focus time over the last 30 days.</li>
  <li><strong>Pie chart</strong> — shows how your focus is distributed across subjects in the last 30 days.</li>
  <li><strong>Pie chart</strong> — shows how your focus is distributed across period settings in the last 30 days.</li>
  <li><strong>Bar chart</strong> — shows the focus time per subject in the last 30 days.</li>
  <li><strong>Bar chart</strong> — same as the previous one, but for all history (archived subjects can be shown or hidden).</li>
</ol>

<h2>Syncing</h2>
<p>monkmode stores all data locally on your device. There are no plans for a built-in cloud syncing feature.</p>

<p>Advanced users can sync their data with third-party cloud services (like OneDrive or iCloud) using junctions / symbolic links.</p>

<h3>Important</h3>
<ul>
   <li>Never open MonkMode on more than one device at the same time when using junctions, to avoid database corruption.</li>
   <li>You must be logged into the same cloud service on all devices and create junctions on each device pointing to the synced folder.</li>
</ul>

<h3>How to set it up</h3>

<h4>Windows</h4>
<p>Data is stored in:</p>
<pre><code>%AppData%\Roaming\MonkMode
</code></pre>

<p>You can create a junction to a cloud folder:</p>
<pre><code>mklink /J "%AppData%\MonkMode" "C:\Users\<YourUser>\OneDrive\MonkModeData"
</code></pre>

<p>Ensure a junction is created on each device pointing to the same cloud folder.</p>

<h4>Linux / macOS</h4>
<p>Data is stored in your home folder, in a hidden folder called <code>.monkmode</code>. For example, <code>/home/username/.monkmode</code> on Linux or <code>/Users/username/.monkmode</code> on macOS.</p>

<pre><code># Python reference
from pathlib import Path
app_data = Path.home() / '.monkmode'
</code></pre>

<p><i>Note:</i> Junctions / symlinks may or may not work reliably for syncing on Linux/macOS. If you try it, ensure the cloud service is the same on all devices and the symlink points to the synced folder.</p>

<p>
<h2>Wrapping Up</h2>
  With this, we’ve covered all the important features. If you have any questions, feel free to ask them in the GitHub repository.
</p>
<p>
  <strong>Happy focusing!</strong> – dop14
</p>


   




























