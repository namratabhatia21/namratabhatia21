<p align="center"><img src="https://capsule-render.vercel.app/api?type=venom&color=0:ff00ff,50:7b2ff7,100:00f0ff&height=260&section=header&text=NAMRATA&fontSize=84&fontColor=ffffff&fontAlignY=40&stroke=00f0ff&strokeWidth=2&animation=twinkling&desc=you%20just%20walked%20into%20a%20puzzle%20box&descSize=20&descAlignY=64" width="100%" alt="NAMRATA - you just walked into a puzzle box"></p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=900&color=FF2E97&center=true&vCenter=true&width=600&height=60&lines=%3E+opening+puzzle_box.exe+...;Shipped+at+work.+Now+building+in+public.;6+rooms.+6+locks.+1+escape+code.;Every+bug+is+a+puzzle+in+disguise.;The+door+just+locked.+Can+you+get+out%3F">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=900&color=C2185B&center=true&vCenter=true&width=600&height=60&lines=%3E+opening+puzzle_box.exe+...;Shipped+at+work.+Now+building+in+public.;6+rooms.+6+locks.+1+escape+code.;Every+bug+is+a+puzzle+in+disguise.;The+door+just+locked.+Can+you+get+out%3F" alt="Typing: opening puzzle_box.exe... Shipped at work. Now building in public. 6 rooms. 6 locks. 1 escape code.">
  </picture>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PUZZLE_BRAIN-MAX-ff2e97?style=for-the-badge&labelColor=0d1117" alt="Puzzle brain: MAX">
  <img src="https://img.shields.io/badge/PAST_COMMITS-classified-7b2ff7?style=for-the-badge&labelColor=0d1117" alt="Past commits: classified">
  <img src="https://img.shields.io/badge/KEYS-0_of_6-f9c80e?style=for-the-badge&labelColor=0d1117" alt="Keys: 0 of 6">
  <img src="https://img.shields.io/badge/NOW-building_in_public-00f5d4?style=for-the-badge&labelColor=0d1117" alt="Now: building in public">
</p>

```console
$ figlet -f "ANSI Shadow" HELLO
██╗  ██╗███████╗██╗     ██╗      ██████╗
██║  ██║██╔════╝██║     ██║     ██╔═══██╗
███████║█████╗  ██║     ██║     ██║   ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝
$ ./boot.sh --player namrata
[ OK ] code shipped at work ....... classified
[ OK ] building in public ........... Agentic
[ OK ] puzzle brain ....................... MAX
[INFO] contribution graph .... just switched on
[SKIP] stats cards .. the good stuff is private
$ cat mission.txt
You opened my profile. The door clicked shut. 🔒
6 rooms. 6 locks. Each answer is a key letter.
Collect all 6 -> crack the vault -> escape.
```

> [!TIP]
> **How to play:** open a door, solve the lock, *then* click 🗝️ **use key**. Rooms 01–06 each give one key letter for the vault. The corridor's number is saved for later. I can't check if you peeked. Your conscience can.

## 🎒 Inventory

<a href="https://github.com/namratabhatia21/Agentic"><img src="https://img.shields.io/badge/ITEM_001-Agentic-00f5d4?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117" alt="Item 001: Agentic"></a>

```diff
@@ inventory.sav @@
+ item_001  = "Agentic"   # my AI-agent experiments
+ curiosity = float("inf")
+ stack     = "whatever the puzzle needs"
- graph     = "sparse"    # commits live in work repos
+ graph     = "growing"   # now shipping in public
```

## 🗺️ Floor plan

<p align="center">
<kbd>🚪 ENTRANCE</kbd> ➜ <kbd>🧩 CORRIDOR</kbd> ➜ <kbd>01</kbd> ➜ <kbd>02</kbd> ➜ <kbd>03</kbd> ➜ <kbd>04</kbd> ➜ <kbd>05</kbd> ➜ <kbd>06</kbd> ➜ <kbd>🗝️ VAULT</kbd> ➜ <kbd>🏁 EXIT</kbd>
</p>

Every room is one of my obsessions, rated by how it grows:

| room | obsession | Big-O | because |
|:--:|:--|:--:|:--|
| 01 | 📚 **Learning** | `O(∞)` | `while True:` · no base case |
| 02 | 🧮 **Algorithms** | `O(1)` | constant love, any input |
| 03 | 🏗️ **System Design** | `O(log n)` | halve it until it fits |
| 04 | 📊 **Data** | `O(n log n)` | sort first, ask later |
| 05 | 🌍 **Open Source** | `O(n²)` | everyone × every idea |
| 06 | 🛠️ **Creating** | `O(n)` | one commit at a time |

<p align="center"><sub>⚠️ <b>cycle detected:</b> CREATING → LEARNING. Not a bug. That's the main loop.</sub></p>

## 🧩 The corridor <sub><code>BFS</code></sub>

The rooms are at the end of this hallway. Step only ↑ ↓ ← →.

<p align="center">
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦<br>
🟦🐣⬜⬜🟦⬜⬜⬜🟦⬜🟦<br>
🟦🟦🟦⬜🟦⬜🟦⬜🟦⬜🟦<br>
🟦⬜⬜⬜⬜⬜⬜🟦⬜⬜🟦<br>
🟦⬜🟦🟦🟦🟦⬜🟦🟦⬜🟦<br>
🟦⬜⬜⬜🟦⬜⬜⬜⬜⬜🟦<br>
🟦🟦⬜🟦🟦⬜🟦🟦🟦⬜🟦<br>
🟦⬜⬜🟦⬜⬜🟦⬜⬜🏁🟦<br>
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
</p>

<p align="center"><sub>🐣 you · 🏁 the doors · 🟦 wall · ⬜ floor</sub></p>

**What's the fewest moves from 🐣 to 🏁?** &nbsp; 📌 *Remember this number. The vault will ask for it.*

<details>
<summary>🗝️ <b>use key</b></summary>
<br>

**14 moves**, and only one route is that short. BFS explores the floor ring by ring, so the first time it touches 🏁 is guaranteed to be the shortest path. 🟡 marks it:

<p align="center">
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦<br>
🟦🐣🟡🟡🟦⬜⬜⬜🟦⬜🟦<br>
🟦🟦🟦🟡🟦⬜🟦⬜🟦⬜🟦<br>
🟦⬜⬜🟡🟡🟡🟡🟦⬜⬜🟦<br>
🟦⬜🟦🟦🟦🟦🟡🟦🟦⬜🟦<br>
🟦⬜⬜⬜🟦⬜🟡🟡🟡🟡🟦<br>
🟦🟦⬜🟦🟦⬜🟦🟦🟦🟡🟦<br>
🟦⬜⬜🟦⬜⬜🟦⬜⬜🏁🟦<br>
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
</p>

</details>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0d1117&height=90&section=header&text=6%20DOORS%20%C2%B7%206%20LOCKS%20%C2%B7%201%20WAY%20OUT&fontSize=32&fontColor=ff2e97&fontAlignY=55&animation=fadeIn" width="100%" alt="6 doors, 6 locks, 1 way out"></p>

<details>
<summary><b>🔒 ROOM 01 · LEARNING</b> &nbsp;·&nbsp; <i>the red teacher</i></summary>
<br>

> I show up in red, usually at the worst possible moment.<br>
> Beginners panic when they see me. Good engineers read me slowly, line by line.<br>
> I am the most honest teacher you will ever have.<br>
>
> **What am I?** &nbsp; `_ _ _ _ _`

<details>
<summary>🗝️ <b>use key</b></summary>

**ERROR** · your letter: <kbd>E</kbd>

I've met plenty of these in work codebases, and I still read every one. Each red line is a free lesson, and I collect them like puzzle pieces. My whole learning strategy: break it, read it, fix it, repeat. 🔁

</details>
</details>

<details>
<summary><b>🔒 ROOM 02 · ALGORITHMS</b> &nbsp;·&nbsp; <i>trace the machine</i></summary>
<br>

No running it. Trace it in your head:

```python
stack = []
for ch in "KCATS":
    stack.append(ch)

print("".join(stack.pop() for _ in range(len(stack))))
```

**What gets printed?** &nbsp; `_ _ _ _ _`

<details>
<summary>🗝️ <b>use key</b></summary>

**STACK** · your letter: <kbd>S</kbd>

Last in, first out: the word comes out reversed, and it names the very structure that reversed it. Algorithms are just puzzles that come with proofs. 🤓

</details>

<details>
<summary>⭐ <b>bonus lock:</b> I'm thinking of a number from 1 to 1000. I answer <i>higher</i>, <i>lower</i> or <i>got it</i>. What's the most guesses binary search will ever need?</summary>

$$\lceil \log_2 (1000 + 1) \rceil = 10$$

Each guess checks one number and throws away the wrong half, so $k$ guesses can cover at most $2^k - 1$ numbers. $2^9 - 1 = 511$ is too few, $2^{10} - 1 = 1023$ is enough. **10 guesses, max.**

</details>
</details>

<details>
<summary><b>🔒 ROOM 03 · SYSTEM DESIGN</b> &nbsp;·&nbsp; <i>the missing box</i></summary>
<br>

```text
 ┌───────┐ request ┌───────────┐  miss  ┌──────────┐
 │  you  ├────────>│ _ _ _ _ _ ├───────>│ database │
 │       │<────────┤     ?     │<───────┤          │
 └───────┘   hit   └───────────┘  slow  └──────────┘
```

> I sit between you and the slow database.<br>
> I remember what you asked recently and answer in a blink.<br>
> When I fill up, I forget whatever you touched least recently.<br>
>
> **Name the missing box.** &nbsp; `_ _ _ _ _`

<details>
<summary>🗝️ <b>use key</b></summary>

**CACHE** · your letter: <kbd>C</kbd>

Hit = ⚡. Miss = 🐢. System design is one giant puzzle of trade-offs. Here are the bosses I've scouted so far. Weaknesses known, swords not yet sharpened:

| 👾 boss | 🗡️ known weakness |
|:--|:--|
| **Thundering Herd** | backoff + jitter |
| **Split-Brain Hydra** | quorum: majority wins |
| **Cache Invalidator** ☠️ | *nobody knows* |

</details>
</details>

<details>
<summary><b>🔒 ROOM 04 · DATA</b> &nbsp;·&nbsp; <i>numbers in costume</i></summary>
<br>

Computers don't store letters. They store numbers wearing letter costumes.<br>
Unmask these five bytes. <sub>(hint: `01000001` = 65 = `A`)</sub>

```text
01000001 01010010 01010010 01000001 01011001
```

**What's the word?** &nbsp; `_ _ _ _ _` &nbsp; <sub>(irony: these bytes would live in one)</sub>

<details>
<summary>🗝️ <b>use key</b></summary>

**ARRAY** · your letter: <kbd>A</kbd>

`A` = 65, `R` = 82, `Y` = 89. Data is the ultimate puzzle box: messy on the outside, patterns on the inside. I'm learning to find them.

</details>

<details>
<summary>⭐ <b>bonus lock:</b> a 4×4 sudoku hiding another data structure</summary>
<br>

Fill every row, column and 2×2 box with **A E H P** (each exactly once). Then read the ↘ diagonal.

```text
╔═══════╦═══════╗
║ ·   A ║ P   · ║
║ P   · ║ ·   A ║
╠═══════╬═══════╣
║ ·   P ║ ·   · ║
║ ·   · ║ E   · ║
╚═══════╩═══════╝
```

<details>
<summary>🔓 <b>reveal the grid</b></summary>

Row by row: <code><b>H</b>APE</code> · <code>P<b>E</b>HA</code> · <code>EP<b>A</b>H</code> · <code>AHE<b>P</b></code>

The diagonal spells **HEAP**: a priority queue, which is exactly how I keep puzzles. The most interesting one is always on top.

</details>
</details>
</details>

<details>
<summary><b>🔒 ROOM 05 · OPEN SOURCE</b> &nbsp;·&nbsp; <i>the ritual</i></summary>
<br>

The open-source ritual has five steps. Step 5 went missing.

```bash
gh repo fork owner/project --clone   # 1. fork it
cd project && git switch -c fix-typo # 2. branch it
git commit -am "docs: fix typo"      # 3. commit it
git push -u origin fix-typo          # 4. push it
# 5. ??? ...politely ask the maintainers to take it
```

**What do you open?** &nbsp; `_ _ _ _   _ _ _ _ _ _ _`

<details>
<summary>🗝️ <b>use key</b></summary>

**PULL REQUEST** · your letter: <kbd>P</kbd> &nbsp; <sub>(`gh pr create`)</sub>

Most of my code has lived behind company walls. Open source is where I get to build with everyone at once. More PRs to other people's projects are the next rooms I'm building. 🎯

</details>
</details>

<details>
<summary><b>🔒 ROOM 06 · CREATING</b> &nbsp;·&nbsp; <i>the shout</i></summary>
<br>

> I'm the word you yell when the bug finally dies, the build turns green, or the puzzle clicks.<br>
> A Greek mathematician famously shouted me from a bathtub.<br>
>
> **What am I?** &nbsp; `_ _ _ _ _ _`

<details>
<summary>🗝️ <b>use key</b></summary>

**EUREKA** · your letter: <kbd>E</kbd>

Creating is chasing that moment on purpose. My current lab is **[Agentic](https://github.com/namratabhatia21/Agentic)**, where I experiment with AI agents. Expect small explosions. 🧪

</details>
</details>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0d1117&height=90&section=header&text=%E2%9A%A0%20VAULT%20DOOR%20%E2%9A%A0&fontSize=36&fontColor=f9c80e&fontAlignY=55&animation=blinking" width="100%" alt="VAULT DOOR"></p>

<p align="center">
<kbd>&nbsp;?&nbsp;</kbd> <kbd>&nbsp;?&nbsp;</kbd> <kbd>&nbsp;?&nbsp;</kbd> <kbd>&nbsp;?&nbsp;</kbd> <kbd>&nbsp;?&nbsp;</kbd> <kbd>&nbsp;?&nbsp;</kbd><br>
<sub>code = the first letter of each key, rooms 01 → 06</sub>
</p>

<details>
<summary>🔓 <b>enter the 6-letter code</b></summary>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00ff,50:7b2ff7,100:00f0ff&height=120&section=header&text=YOU%20ESCAPED&fontSize=48&fontColor=ffffff&fontAlignY=42&animation=blinking&desc=code%20accepted%3A%20E%20S%20C%20A%20P%20E&descSize=18&descAlignY=78" width="100%" alt="YOU ESCAPED - code accepted: E S C A P E"></p>

<p align="center"><kbd>E</kbd> <kbd>S</kbd> <kbd>C</kbd> <kbd>A</kbd> <kbd>P</kbd> <kbd>E</kbd></p>

```diff
- status : trapped in namrata's profile
+ status : ESCAPED
+ keys   : 6 of 6
+ found  : a fellow puzzle person. hi! 👋
```

<details>
<summary>🤫 <i>...wait. There's an envelope taped under the desk.</i></summary>
<br>

```text
BCK PIWZRWBU WB DIPZWQ
```

<sub>hint: a Caesar shift. The key is your answer from the corridor. Slide every letter <b>back</b> that many places (A wraps to Z).</sub>

<details>
<summary>📜 <b>decrypt</b></summary>

<sub>shift = 14 moves &nbsp;·&nbsp; B → N, C → O, K → W ...</sub>

<h3 align="center">NOW BUILDING IN PUBLIC.</h3>

<p align="center">
Most of my solved puzzles are locked in private work repos. From here on, they get solved in the open.<br>
New rooms unlock as I build. Come back and try them. 🧩
</p>

**🚧 rooms under construction**

- [x] ship code at work <sub>(private, so you'll have to trust me)</sub>
- [x] start building in public
- [x] build room 001: [Agentic](https://github.com/namratabhatia21/Agentic)
- [x] lock visitors inside this puzzle box
- [ ] open pull requests on other people's projects
- [ ] room 07 · `???` *(unlocks at level 2)*

</details>
</details>
</details>

<p align="center"><sub>built by someone who reads error messages for fun · most of my code lives in private work repos · the puzzles live here</sub></p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:00f0ff,50:7b2ff7,100:ff00ff&height=150&section=footer&text=CONTINUE%3F%20%E2%96%B6%20YES&fontSize=34&fontColor=ffffff&fontAlignY=68&animation=blinking" width="100%" alt="CONTINUE? YES"></p>
