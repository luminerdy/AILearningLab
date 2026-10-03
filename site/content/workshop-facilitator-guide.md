# AI Learning Lab: Instructor Guide

Students use AI to learn something unfamiliar, build a small working project, and create a DIY or STEM outreach lab that helps someone else learn. Raspberry Pi 500 workstations with Codex CLI are the workshop environment. USB cameras, Raspberry Pi Pico, and PicoBot are optional instructor-prepared routes.

This is a first-pass curriculum for piloting. Plan initially for **three two-hour sessions**; these are estimates, not measured completion times. Hardware projects may need additional sessions. A three-hour introduction can cover the warmup, a small first build, and initial checks; it should not promise the complete project and teaching lab.

## Learning outcomes

- I can use AI to make progress on something unfamiliar, ask useful questions, check its guidance, and decide what to try next.
- I can use AI to create and test a DIY or STEM outreach lab for another learner.

Look for prediction, observation, explanation, revision, and evidence of increasingly independent choices. A polished project alone is insufficient. Students need not write every line themselves or understand every implementation detail, but should explain important behavior and know how to investigate uncertainty.

## Prepare the classroom

Before enrollment, confirm account eligibility, school requirements, sign-in arrangements, and expected usage limits. Do not assume the previously discussed subscription arrangement is settled. Test the full Codex CLI installation and authentication on the actual Pi 500 operating-system image and classroom network. Follow [official Codex CLI documentation](https://learn.chatgpt.com/docs/codex/cli).

Prepare one project folder per student, a working Python environment, an editor, Git, and tested run commands. Rehearse opening a terminal, starting `codex`, inspecting files, saving a checkpoint, and restoring a working version. Prepare a known working sample and saved AI responses for access interruptions. AI access is needed for the full intended experience; an offline fallback can practice checking but does not replace it.

Use an instructor-prepared project instruction file to state the exact environment, allowed changes, and learning habits. Ask for small steps and explanations; require confirmation before hardware actions or system changes. Show students how permissions affect edits and commands rather than asking them to approve unfamiliar commands blindly. Use sample data and keep credentials outside shared projects.

Pilot one Pi-only project and one optional Pico project. Verify camera models, Pico firmware, pin assignments, wiring, libraries, and robot hardware against the actual kit and manufacturer documentation. Do not let generated instructions substitute for checked wiring. Review wiring before power; test motor actions in a cleared area with a reliable stop method. Begin with controlled movement before adding sensing.

Provide the [student workbook](workshop-student-workbook.md), shared display, materials inventory, and submission location. No coding experience is required; teach the few terminal and file actions students need at the moment they use them.

## Participation and project scope

Students complete every lab individually, with open conversation and help around the room. Peer trials are optional. Each student keeps their own learning record. Choose an unfamiliar task with observable outcomes and a small first version. Help students reduce scope before building; offer a Pi-only route to everyone, including students waiting for hardware.

Use [Code & Create Lab](https://github.com/stemoutreach/CodeCreateLab) as inspiration for guides, small builds, checklists, and extensions. Its README describes Python, Pico breadboarding, and PicoBot routes. Include attribution when reusing materials. The example ideas in this workshop are not complete tested hardware labs.

## Teaching sequence and proposed timing

Open the [workshop overview](https://luminerdy.github.io/AILearningLab/workshop.html). Students follow the website's Previous and Next links.

| Session | Minutes | Activity and evidence |
|---|---|---|
| 1: Ask and Explore | 0–15 | Welcome, starting point, workstation and access check |
| | 15–30 | [LLM basics](llm-basics.md): tokens, context, hallucinations, unsupported-detail activity |
| | 30–40 | Announcement warmup: compare AI output with supplied facts |
| | 40–55 | Demonstrate a small build, prediction, check, and focused change |
| | 55–65 | Break |
| | 65–85 | Choose unfamiliar project; write three observable criteria |
| | 85–110 | Discuss plan with AI; build and try first version |
| | 110–120 | Save work, observations, checkpoint, and next question |
| 2: Build, Check and Adjust | 0–10 | Reopen work and run saved version |
| | 10–40 | Check normal use, unusual conditions, and repetition |
| | 40–55 | Investigate one finding; make and recheck a focused change |
| | 55–65 | Break |
| | 65–100 | Independent small extension using AI and available help |
| | 100–120 | Demonstrate behavior, record limits, and save working version |
| 3: Create a Lab and Teach | 0–15 | Choose audience and learning goal |
| | 15–45 | Draft lab from actual code, checks, and equipment |
| | 45–55 | Review instructions, explanation questions, and assumptions |
| | 55–65 | Break |
| | 65–95 | Self-trial or optional learner trial; record confusion and results |
| | 95–110 | Revise and recheck lab instructions |
| | 110–120 | Demonstrate, reflect, and choose next learning step |

For a three-hour taster: welcome/access 15 minutes, LLM basics 15, warmup 10, demonstration 15, project definition 20, first build 35, break 10, checks/revision 35, reflection/save 25. Schedule the lab-writing and trial session afterward. Simplify the first build if access or hardware troubleshooting consumes time.

## Lab 1: Ask and Explore

Begin: “Choose something you want to learn but do not yet know how to do. AI can help you build it. You will decide what should happen, check what happens, and turn your learning into an activity for someone else.”

Keep the announcement warmup short. Verify all seven supplied fact groups and the 100-word limit; do not depend on AI producing an error. If it is accurate, improve clarity and recheck.

Demonstrate a tiny quiz or two-choice story in a prepared project folder. Describe the goal, ask AI to clarify and plan, then authorize a small version. Predict an outcome before running. Try a known answer and an invalid input. Ask for an explanation and one focused improvement. Show a checkpoint and the changed files.

Prompt students: “What don't you know yet?” “What is the smallest version?” “How could you tell if it worked?” Keep AI explanations short enough to use. Students should save questions that changed their understanding, not only successful prompts.

## Lab 2: Build, Check and Adjust

Ask students to write expected outcomes before running checks. Require evidence from the actual program or device. For a quiz, try known correct and incorrect answers and restart; for a capture tool, inspect the saved file. Help students translate “it doesn't work” into steps, expected behavior, actual behavior, and exact errors.

Encourage one investigative check before a broad rewrite. Compare automated tests with the student's criteria. Make an extension small enough that students can predict and observe its effect. Independence includes seeking useful help; do not withdraw support to prove independence.

## Lab 3: Create a Lab and Teach

Students give AI actual project files and evidence, then draft for a named audience. Require learning questions and expected observations, not just commands to copy. Review setup, file names, dependencies, hardware details, and claims of testing.

A self-trial is required; another learner's trial is encouraged when feasible. Students must label which occurred. Watch for missing steps and whether the learner can explain the target idea. Recheck instructions after revisions. A STEM outreach version should fit the audience's time, vocabulary, supervision, and available equipment.

## Evidence and assessment

| Outcome | Evidence |
|---|---|
| Define | An unfamiliar learning goal, small version, equipment context, and three criteria |
| Direct | Questions, reviewed plan, and requests suited to the next step |
| Check | Expected and actual results from observable behavior or other independent evidence |
| Adjust | A finding-linked change and repeated checks |
| Learn independently | A chosen extension, useful help-seeking, prediction, and explanation |
| Teach | Audience-specific lab, trial record, and improvement based on the trial |

Final submission: working project and run instructions; reusable lab; project checks; lab trial and revision; reflection and credits. If unfinished, accept an honest account of demonstrated behavior and remaining work, and arrange a continuation rather than claiming completion.

## Pilot and improve

Record setup delays, scope reductions, questions that helped learning, checks students could perform independently, trial confusion, and time needed per route. Ask students what they now feel able to investigate. Revise the estimates and materials from that evidence before expanding hardware choices.

Use the [learning map](https://luminerdy.github.io/AILearningLab/progression.html) for reflection. ASK is an entry point; learners move among practices rather than earning a maturity score. See the [full framework](agentic-ai-learning-progression-updated.md) and [continued learning](learning-path.md).
