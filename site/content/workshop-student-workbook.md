# AI Learning Lab: Learn, Build, Teach

Use AI to learn something you do not know how to do. Build a small working project, check and improve it, then create a DIY or STEM outreach lab that helps another person learn.

**Define → Direct → Check → Adjust**

Two outcomes to work toward:

- I can use AI to learn something unfamiliar, check its guidance, and decide what to try next.
- I can use AI to create and test a lab that helps others learn.

Work individually on a Raspberry Pi 500 with Codex CLI. Talk with classmates and ask for help. Keep your own project, requests, evidence, and lab. Your instructor provides the prepared workstation and sign-in instructions. Optional hardware is available only when your instructor has prepared it.

## Your starting point

What would I like to learn to make or do?

What can I already do, and what do I not understand yet?

What could I observe to tell whether it works?

Mark ASK and COLLABORATE as comfortable and repeatable / experimented with / want to learn next. These describe experience, not a ranking.

## LLM basics warmup

Read [LLM basics](llm-basics.md) and complete its unsupported-detail activity.

Explain a token in your own words. Why can a fluent response still need checking? Identify one supported, contradicted, and unsupported detail in the practice response.

## Lab 1 Ask and Explore

**Goal:** Choose something unfamiliar but achievable, define a small first version, and use AI to begin learning and building it.

### Quick warmup: check supplied facts

Code and Create Club meets Thursday, 3:30–4:15 p.m., in Room 204. Beginners are welcome. Materials are provided. There is no fee. Capacity is 20 students. Sign up with the club adviser by Wednesday.

Ask Codex for an announcement of at most 100 words containing all these facts. Check the facts and count the words yourself. Ask for a focused correction or clarity improvement and check again. Spend about ten minutes here, then move to your project.

### Choose your project

Choose something you want to learn and cannot already build independently. You should be able to observe whether a small version works.

| Route | Example idea | First version | Something you can check |
|---|---|---|---|
| Pi 500 only | Treasure hunt | Two choices and one ending | Each choice reaches the expected ending |
| Pi 500 only | STEM quiz | Three questions and a score | Known answers give the expected score |
| Pi 500 only | Reaction game | Start, signal, response, reset | Early input is rejected and reset works |
| USB camera, if prepared | Stop-motion capture | Capture and save one image | The saved image opens and matches the scene |
| Pico, if prepared | Button and LED | One button changes one light | Pressing and releasing match the intended behavior |
| PicoBot, if prepared | Controlled movement | Short forward movement and stop | It stops as instructed in a cleared test area |

These are project ideas, not tested hardware instructions. Propose your own idea too. Confirm the first version and available equipment with your instructor. Add extensions after the first version works.

### Define a small success

My project and intended user:

Something I want to understand:

My smallest useful version:

My exact equipment and software, supplied by the instructor:

| Success criterion | How I can check it |
|---|---|
| 1 | |
| 2 | |
| 3 | |

### Meet your workspace

Use the project folder your instructor gives you. Open a terminal there and start `codex`. Sign in using the provided account instructions. Ask what files are present before requesting changes. Ask your instructor before changing permissions, installing system software, or using hardware you have not checked.

Your instructor shows you how to save a Git checkpoint and return to a known working version. Keep credentials and personal information out of the project and final lab.

### Direct AI to help you learn

> I want to learn how to create [project], but I do not know [unknown]. My equipment is [exact details]. Ask me a few questions to clarify the goal. Propose the smallest working version and explain what I should observe. Help me choose three checks I can perform. Identify assumptions and missing information. Do not build until we have discussed the plan.

My actual request and useful follow-up questions:

What assumptions did we resolve?

After reviewing the plan:

> Build only this first version in my project folder. Explain the files and how to run it. Use small steps. Tell me what I should expect and pause before hardware actions or changes outside this folder. Draft brief lab notes, marking anything we have not tested.

Save your request, plan, first code, and run instructions. AI may write code; your job includes understanding the behavior and checking the result.

### Predict, try, explain

Before running: What do I expect to happen?

After running: What actually happened?

Ask AI to explain one important piece. Use that explanation to guide an experiment; the explanation itself is not proof.

What did I learn? What do I still need to investigate?

**Save:** Your goal, three criteria, plan, first version, and first observations. Checking begins here and continues in Lab 2.

## Lab 2 Build, Check and Adjust

**Goal:** Establish evidence for your project, investigate problems, and make a checked improvement.

### Check observable behavior

Use your Lab 1 criteria. Include normal use, an unusual or invalid input, and restarting or repeating the activity where relevant. Write expected results before trying each check.

| Check and steps | Expected result | Actual result and evidence | Next action |
|---|---|---|---|
| Normal use | | | |
| Unusual input or condition | | | |
| Repeat or restart | | | |

Save an error message, screenshot, measured observation, or other useful evidence. AI-run tests can help; compare them with your own criteria and actual project behavior. Code running without errors does not establish that it meets your goal.

### Investigate instead of guessing

> I expected [result] when I [steps]. Instead I observed [result]. Here is the exact error or evidence: [details]. Help me investigate. Explain likely causes and suggest one check that distinguishes them before changing the code.

My finding and the evidence behind it:

My focused change request:

What changed? Which checks did I repeat, and what did they show?

Use a saved checkpoint if a change makes things worse. Ask for help when you cannot explain the next action.

### Show understanding through a change

Choose a small change: add a question, alter a rule, change a timing setting, or improve feedback. Predict its effect, ask AI for help, and test your prediction. Do not change wiring or motor behavior without the instructor's hardware review.

My prediction:

My observation and explanation:

### Your independent extension

Choose one small extension without step-by-step instructor directions. You may use AI, classmates, documentation, and instructor help. Independence means choosing your next useful action and evidence, not refusing help.

What I chose, why, and what I needed to learn:

My request, checks, and adjustment:

**Save:** A working project, run instructions, check results, a documented improvement, and an honest list of limitations. If unfinished, state exactly what works and what still needs investigation.

## Lab 3 Create a Lab and Teach

**Goal:** Turn your tested project into a DIY or STEM outreach activity another learner can follow.

### Define your learner

Who is the lab for? What can they already do?

What should they understand or be able to do afterward?

How much time and what equipment will they have?

### Ask AI to draft from your evidence

> Help me create a DIY or STEM outreach lab for [audience] using my project. The learning goal is [goal]. Use my actual code, equipment, run instructions, and recorded checks. Include materials, setup, numbered steps, expected observations, explanation questions, troubleshooting, and one extension. Separate verified steps from untested suggestions. Do not invent successful test results. Keep the first activity small enough for [time].

Read every step. Correct assumptions and match file names and commands to your actual project. Include instructor-reviewed hardware instructions when needed.

### Your lab template

1. **Title and learning goal:** What will the learner understand or do?
2. **Audience and prerequisites:** Who is this for, and what must they already know?
3. **Materials and setup:** Exact equipment, software, files, and preparation. State whether learners need AI access.
4. **Steps:** Numbered actions with expected observations and checks.
5. **Learn while doing:** Prediction and explanation questions, with facilitator reference answers checked by you.
6. **Troubleshooting:** Observed problems, ways to investigate, and when to ask for help.
7. **Challenge:** One optional extension with a clear check.
8. **Evidence and limits:** What was tested, what remains uncertain, and relevant hardware precautions.
9. **Credits:** Identify AI assistance and any reused sources, including Code & Create Lab when used.

### Try the instructions

Run through the lab from its stated starting setup using only its written instructions. If possible, invite a classmate or instructor to try it; this is optional and does not require assigned partners. Do not describe a self-trial as a trial with another learner.

| Step | Who tried it | Expected result | Observation or confusion | Revision and recheck |
|---|---|---|---|---|
| | | | | |

Ask the trial learner what they learned, not only whether the project ran. If you trial it yourself, answer the explanation questions and identify where a beginner might need more context.

### Final demonstration and reflection

Show the working project, demonstrate one check, explain one revision, and share your lab and its trial evidence. Use the class submission method; public posting is not required.

1. What could I not do at the beginning that I can now do or explain?
2. Which question helped me learn most?
3. What AI guidance did I verify, correct, or leave uncertain?
4. What evidence supports the project's behavior?
5. What changed after trying the lab instructions?
6. What would I try next when learning something unfamiliar?

**Save:** Code and run instructions, your reusable lab, test and trial records, and your reflection. Record what you contributed and what AI contributed.

Mark ASK, COLLABORATE, ORIENT, and capturing reusable know-how as comfortable and repeatable / experimented with / want to learn next. You do not need to reach ORCHESTRATE.

**Start where you are. Move one step.**
