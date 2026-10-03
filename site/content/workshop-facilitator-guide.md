# AI Learning Lab ASK Workshop Facilitator Guide

This first workshop teaches students to use AI for a small, useful task and judge the result. Students leave with an initial request, a checked result, a revision, and evidence explaining what improved. The central habit is **Define → Direct → Check → Adjust**.

The live introduction is three hours for high school beginners, adaptable to older learners. It can be split into three one-hour classes and expanded into several days using the [follow-on labs](learning-path.md). No coding experience is required. Use the [student workbook](workshop-student-workbook.md) during the session. The website provides continued learning beyond the live workshop.

## Learning outcomes

By the end, students should be able to:

- Describe a task, its audience, relevant information, and constraints.
- Ask AI for a useful result and revise the request after inspecting the answer.
- Check a result against at least three criteria using supplied facts or observable evidence.
- Explain one limitation and choose a useful next practice.
- Explain that text is generated token by token and that fluent answers can contain false or unsupported details.

ASK is the entry point. Iteration introduces COLLABORATE naturally. Show the full progression only briefly at the end; students do not need to reach its final stage.

## Preparation

Provide a school-approved AI tool, the student workbook, a timer, and a shared display. Follow the school's existing access and academic-use rules. Use the fictional scenario below so participation requires no personal information or uploads. Test the scenario in the chosen tool before class; save one response for a demonstration if access fails. AI responses will vary, so the answer key checks requirements rather than exact wording.

Tell students which AI tool and account they need before the workshop. Confirm student account eligibility and school requirements when preparing enrollment instructions. The opening exercises use ordinary text requests and supplied facts.

Each student completes every lab individually, including directing AI, checking, and revising. Encourage open conversation, questions, and comparing approaches around the room. Students keep their own requests, artifacts, and evidence. There are no assigned partners or role switches; feedback from others is optional. If only the instructor has access, students write individual requests on paper, select several to run on the shared screen, and independently check the displayed output. If no AI is available, use a saved response to practice checking and write the next request students would send.

## Session agenda

Open the [workshop overview](https://luminerdy.github.io/AILearningLab/workshop.html) as the shared teaching entry point. Students can follow the Previous and Next links without leaving the website.

| Workshop page | Teaching focus | Agenda minutes |
|---|---|---|
| [LLM Basics](https://luminerdy.github.io/AILearningLab/llm-basics.html) | Terminology, prediction, context, and hallucinations | 10–25 |
| [Lab 1 Ask](https://luminerdy.github.io/AILearningLab/lab-1-ask.html) | Demonstrate, define a goal, and make a first request | 25–60 |
| [Lab 2 Check and Adjust](https://luminerdy.github.io/AILearningLab/lab-2-check-adjust.html) | Inspect evidence, revise, and recheck | 70–95 |
| [Lab 3 Your Challenge](https://luminerdy.github.io/AILearningLab/lab-3-challenge.html) | Apply the loop, review, and reflect | 95–125 and 135–170 |
| [Keep Learning](https://luminerdy.github.io/AILearningLab/labs.html) | Choose a follow-on lab | 170–180 |

| Minutes | Activity | Evidence of learning |
|---|---|---|
| 0–10 | Welcome, access check, ASK, and starting self-assessment | One task the student wants help with |
| 10–25 | LLM basics and unsupported-detail activity | Students explain tokens and identify unsupported claims |
| 25–40 | Demonstrate the learning loop | Class identifies a failure and a revision |
| 40–60 | Students individually create and check a club announcement | Three checks with expected and actual results |
| 60–70 | Break | |
| 70–95 | Revise and recheck the first lab | Saved before and after results |
| 95–125 | Students complete an independent challenge | A useful artifact and documented evidence |
| 125–135 | Break | |
| 135–155 | Review results, discuss findings, and revise | An evidence-based finding and a response |
| 155–170 | Share evidence and complete the exit ticket | Evidence of a full loop |
| 170–180 | Introduce the continued learning path and self-location | A selected follow-on lab |

For three one-hour classes, use class one for the opening, demonstration, and first individual response; class two for revision and the independent challenge; class three for individual review, room discussion, reflection, and the next lab. Use the break time in this version for recaps and saving work between classes.

## Opening script

“Today you will use AI to help with a task. Your job is to decide what you want, give useful direction, and check what comes back. A polished answer can still miss a requirement. Keep asking: What would convince me this is right?”

Ask students to complete the starting self-assessment in their workbook. Explain that it describes current experience, not a score or ranking.

## Introduce LLM basics

Use [LLM basics](llm-basics.md) for the 15-minute introduction. Spend about four minutes on LLMs and tokens, three on the sentence-completion analogy and context, five on hallucinations and the deliberately written practice response, and three on terminology and an individual explanation.

Emphasize “next token” rather than always “next word.” Describe prediction as the text-generation mechanism without treating it as a complete account of everything a modern AI system can do. Keep model architecture, training mathematics, and token accounting outside this introductory session.

Use the fixed practice response so the activity works even when a live AI answer contains no errors. Distinguish false statements from details unsupported by the supplied facts. Connect both to checking. Asking the model to be accurate or to avoid guessing does not replace evidence.

## Shared scenario

These are fictional planning facts for a school club event:

- Event: Code and Create Club introductory meeting.
- Day and time: Thursday, 3:30–4:15 p.m.
- Location: Room 204.
- Audience: students curious about making things with technology.
- Beginners are welcome; no coding experience is needed.
- Materials are provided; students do not need to bring a device.
- Capacity is 20 students.
- Sign up with the club adviser by Wednesday.
- There is no fee.

The announcement must include the event name, day, start and end times, location, beginner welcome, materials information, capacity, signup deadline and method, and no-fee information. It must be at most 100 words and invent no additional facts.

## Demonstrate the loop

Start with “Write an announcement for a school technology club meeting.” Before sending it, ask what information is missing. Inspect the answer together. Missing details or invented facts are useful findings; do not depend on the model making a specific mistake.

Then define the goal: “A student should know whether this event is for them and how to attend.” Read the supplied facts and acceptance criteria. Send this second request:

> Write a friendly announcement for students curious about making things with technology. Use only the event facts below. Include every required detail, stay within 100 words, and do not invent a link, date, activity, or contact name. If a necessary detail is missing, ask me. Event facts: [paste the shared scenario facts].

Check the result directly against the scenario. Count the words using an editor or manual count; asking AI for a word count alone does not establish it. If it fails a criterion, identify the actual failure and ask for a targeted revision. Check the revision again.

Explain that providing useful context is part of making a good request. Students do not need to learn AGENTS.md or tools to do this exercise.

## Guide individual practice

Students create their own request from the scenario, save the response, and record at least three checks. Everyone checks factual fidelity, completeness, and word count. Students identify the signup method and deadline in their announcement. They may ask a classmate to read it for additional feedback.

Ask: “Which sentence supports that finding?” “What did you compare it with?” “What would you change in your request?” When a result already meets the criteria, students can improve clarity or explore a different tone while keeping the facts intact. Recheck after every revision.

At minute 70, students resume their own lab and revise from their findings. Avoid treating longer prompts as automatically better; assess whether the direction and evidence are useful.

## Independent challenge

Students choose one task using the same supplied facts:

1. **Event FAQ:** Create five questions and answers covering audience, timing and location, materials, signup and capacity, and cost. Check every answer against the facts and verify that no unsupported details were added.
2. **Preparation checklist:** Create a checklist for a student deciding whether and how to attend. Distinguish stated facts from suggested actions. Check that signup by Wednesday and the Thursday meeting appear, and that bringing a device is not described as required.
3. **Announcement for a new reader:** Create an announcement for someone unfamiliar with the club, at most 80 words. Include the same required details. Check the facts, count words, and identify the signup instructions themselves, optionally asking a classmate for feedback.

Each student defines three criteria before sending a request, saves a response, records checks, and makes at least one evidence-driven revision. They may revise the request or the artifact, but must explain which they changed and recheck the final result. If criteria were already met, the revision can improve clarity based on a reader's feedback.

## Review and assessment

Students review their own goal, criteria, and final artifact, recording one finding with specific evidence. Encourage open discussion and optional feedback from classmates or the instructor. Each student makes a change or explains why the evidence supports keeping the result, and records where the finding came from.

Use this evidence checklist to identify support needs. It evaluates the task, not the student's place on the progression.

| Outcome | Evidence to look for | If evidence is missing |
|---|---|---|
| Define | A goal and three checkable criteria written before requesting | Help replace “good” with a concrete condition |
| Direct | A request containing relevant facts and constraints | Ask which missing information the AI would need |
| Check | Expected and actual results tied to facts or observation | Ask the student to demonstrate one check |
| Adjust | A revision linked to a finding and a second check | Compare versions and identify what changed |
| Reflect | A limitation and a useful next step | Ask what still needs evidence |

A polished final artifact alone does not demonstrate all four habits. Use the saved process and exit ticket to decide what to revisit.

## Closing and self-location

Show **ASSIST → SUGGEST → ASK → COLLABORATE → ORIENT → TEACH → ENABLE → DELEGATE → ORCHESTRATE**. Explain that ASSIST and SUGGEST describe historical developer experiences. Learners can enter at ASK and move among practices according to their needs.

Students mark ASK and COLLABORATE as comfortable, experimented, or a desired next practice. They can name another practice they want to explore, but there is no requirement to progress toward ORCHESTRATE.

Explain how checking can grow: observe behavior; inspect important pieces; collect systematic evidence; use engineering checks when dependable systems require them. This workshop practices checking against supplied facts and criteria. AI's explanation of its own answer is not independent proof.

## Improve the next session

After the pilot, record where students got stuck, which checks they could perform independently, how AI access affected participation, and whether the timing worked. Collect one specific improvement suggestion from students. Use that evidence to revise the workshop before adding more stages.

## Learning framework

Use the [human learning progression](agentic-ai-learning-progression-updated.md) to explore the inclusive ASK entry point, self-location approach, checking model, and iterative learning philosophy. The workshop applies these ideas through a fictional event, individual practice, and evidence-based reflection.

