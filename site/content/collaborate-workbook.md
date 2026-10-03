# COLLABORATE Student Workbook

Improve a small working project and its teaching lab through conversation, evidence, and focused changes. **Define → Direct → Check → Adjust** continues throughout.

Work individually and ask classmates or your instructor for help. AI can suggest options, explain code, and make edits. You decide what to try and establish whether it helped. Keep code-only projects small; hardware is optional.

## Lab 1 Notice and Compare

**Goal:** Find a specific difficulty and choose a bounded improvement. **Planning estimate: 50–60 minutes.**

### Establish a baseline

Open your small project and its instructions, or an instructor-prepared starter. Completing ASK is not required. If you have no lab yet, save the run instructions as your starting notes; you will create a teaching lab in Lab 3. Save a checkpoint with the instructor's demonstrated method. Run the current version using its written instructions. Do not start by asking AI to rewrite it.

Project and learning goal:

Current version or checkpoint:

How to run it:

What already works, with evidence:

One thing I still do not understand:

### Find something worth improving

Trial your lab or starting run instructions yourself, or invite a classmate to try it if available. Note what actually happened. A specific error, confusing step, missing explanation, or awkward interaction is useful evidence. Label whether the observation came from you or another learner.

| Action or lab step | Expected behavior or understanding | Actual observation | Who observed it |
|---|---|---|---|
| | | | |

Use the format: **When [action], I expected [result], but observed [result].** If everything works, choose a learning improvement you can check, such as clearer feedback or an explanation question.

### Bound your change

My one improvement:

Who it helps and why:

What stays outside this change:

What I want to learn by doing it:

| Check | Expected result | How I will observe it |
|---|---|---|
| Desired improvement | | |
| Existing behavior to preserve | | |
| Unusual input, repeat, or restart | | |

### Compare before building

> Here is my project, learning goal, and observation: [details]. Help me investigate before editing. What information is missing? Suggest two small approaches to this one improvement. Compare how each helps the learner, what could go wrong, and how I could check it. Keep [scope limit]. Do not change files yet.

Record the question that helped most. Verify assumptions against your files or actual behavior; an AI explanation is a lead to investigate.

| Approach | Expected benefit | Cost or difficulty | Risk or uncertainty | Check I can perform |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

My chosen approach and reason:

What I rejected or deferred:

**Save:** Baseline, observation, scope, three checks, and decision. If the problem is unclear, do one small investigation before choosing an implementation.

**Optional stretch:** Propose a third approach yourself and compare it using the same evidence. Do not add features simply to make the project bigger.

## Lab 2 Change and Check

**Goal:** Make one focused improvement and decide from evidence whether to keep it. **Planning estimate: 60–75 minutes.**

### Request the smallest useful change

> We chose [approach] because [reason]. Implement only [bounded change]. Preserve [existing behavior]. Tell me which files you expect to change and explain the important edits. Ask before expanding scope. Our checks are [criteria]. Report what you tested and what remains untested.

My actual request:

Before running, I predict:

Files and behavior that changed:

One edit I can explain in my own words:

Ask AI to explain unfamiliar parts, then inspect the files or try a small experiment. You do not need to explain every line to begin checking.

### Test against your baseline

Run the checks you wrote in Lab 1. Record outcomes yourself. Compare any AI-run tests with your actual criteria and observe the program's behavior directly.

| Steps or input | Expected result | Before result | After result and evidence | Keep or investigate |
|---|---|---|---|---|
| Improvement | | | | |
| Preserved behavior | | | | |
| Unusual input, repeat, or restart | | | | |

For a quiz, a correct answer, incorrect answer, and restart may be useful. For a story, follow each branch. For a simulation, check known boundary values. With hardware, use instructor-reviewed actions and actual device observations.

### Give useful feedback

> When I [steps], I expected [result], but observed [result]. Here is the evidence: [error, screenshot, or measurement]. Help me identify the cause. Suggest one distinguishing check, then make a focused correction after we discuss the finding. Avoid unrelated changes.

Finding and evidence:

What I asked next and why:

Revised result and repeated checks:

If the change already meets your criteria, document why you kept it. You do not need to invent an error or make an unnecessary correction. Revert to your baseline when useful and record what you learned.

### Explain your decision

Did it improve the learner's experience or project behavior? What evidence supports that claim?

What remains uncertain?

**Save:** A checked version, before/after evidence, and your decision to keep, revise, or revert the change.

**Optional stretch:** Add one meaningful automated check with AI's help. Inspect what it checks, predict its result, and show that it can detect the relevant failure using a temporary reversible change. Restore and rerun before finishing.

## Lab 3 Improve and Teach

**Goal:** Update your teaching lab to match the improved project and test whether the instructions help a learner. **Planning estimate: 60–75 minutes.**

### Revise from what actually changed

Name your audience and learning goal. Give AI your current code, lab, and check results. Decide which instruction, explanation, or troubleshooting step needs revision.

> Revise my lab for [audience] to match this checked project change: [details]. Use the actual files, run steps, and observations. Preserve [learning goal]. Add a prediction question, an explanation question, and troubleshooting based on our observed issue. Mark suggestions we have not tested. Do not claim that another learner tried it unless my record shows that.

My request:

My edits to the AI draft and why:

### Check the teaching content

| Check | Evidence or correction |
|---|---|
| File names, commands, equipment and steps match the project | |
| Expected observations match my tested behavior | |
| Explanation and reference answers are supported by a run, inspection, or checked source | |
| A beginner can tell what to do when the observed problem occurs | |
| Untested suggestions and known limits are labeled | |

Include learning questions that require prediction and explanation, rather than only copying commands.

### Trial and adjust

Use the written instructions from their stated starting setup. A self-trial is required; another learner's trial is optional. Record who tried it. Let a trial learner use the instructions before offering coaching; note when help was needed.

| Step | Who tried it | Expected observation or learning | Actual result or confusion | Change and recheck |
|---|---|---|---|---|
| | | | | |

Ask: “What did you learn?” and “What would you try if this went wrong?” In a self-trial, answer those questions and identify where a beginner might need help. Be honest about what the trial establishes.

### Demonstrate and reflect

Show the project improvement and one repeated check. Share the revised lab and trial finding.

- Which question or feedback made the AI conversation more useful?
- What did I accept, challenge, or redirect—and why?
- What could I now investigate with less instructor guidance?
- What evidence supports the improvement? What does it not establish?
- How did I help the next learner understand, rather than just finish?

**Submit:** The updated project, before/after checks, focused conversation excerpts, revised teaching lab, trial record, and reflection. Identify AI contributions and credit reused materials. Use the class submission method; public posting is optional.

**Optional stretch:** Adapt the same tested lab for a shorter outreach session or a different audience. Trial the adaptation and preserve its learning goal.

Mark COLLABORATE as comfortable and repeatable / experimented with / want to learn next. Choose another useful practice from the [learning map](https://luminerdy.github.io/AILearningLab/progression.html). ORIENT is a possible next workshop, not a required advancement.
