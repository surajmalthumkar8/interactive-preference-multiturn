# Tasking Instruction

# **CONTRIBUTOR GUIDE**

## Interactive Preference Collection \- Multi-Turn SxS Response

Your task is to build a natural conversation with an AI model over 10–15 turns. For each turn, *write a prompt, compare the model's responses, and select the one you prefer to continue the conversation*.

For this task, we want to see how the model handles **real back-and-forth conversations.** You will need to continue the conversation for 10-15 turns. 

You can use your own real-world prompts and see how the model responds. The **best source** is your actual AI conversation history from **ChatGPT, Gemini, Claude, Copilot, or similar tools.** Copy prompts you've genuinely used before or think of something you've been meaning to work on in your day-to-day.

Keep the conversation going: ask follow-ups, refine the output, push back, change direction, or go deeper. After each turn, you'll compare two responses side by side and choose which one you prefer. Please remove any sensitive or confidential information before submitting. 

We're looking for **authentic** interactions that reflect how you actually use AI. Prompts don't need to be polished; just avoid conversations that are intentionally short or repetitive.

> **Update — per leadership Slack update:** Using AI to help write prompts/turns for this task is now allowed, including **Claude Code**. Any AI-assisted prompt still **must be humanized** before it goes into Feather (see *Human Authenticity* below) — it has to read like something you'd genuinely type, typos and all. This supersedes the "write it yourself from scratch" framing elsewhere in this doc.

Before diving into the task requirements, let’s first cover (1) the tools and (2) basic context you’ll need to get started.

### The Two Platforms

We use two platforms: **Vercel** (Data Annotation Platform) and **Feather**. Claim your task in Vercel first. That is where you will find the link to Feather. Only in Feather do you write prompts and choose between model responses.

* **Always start in Vercel, then go to Feather**  
* **Never work in Feather alone.**  
* **Never work only in Vercel.**

Breaking this sequence can corrupt the data, get you removed from the project, and prevent your tasks from being invoiced correctly. For a safe workflow, check the [**From Start to Submit**]() section.

If you have questions about communicating with the team, payments, or keeping your accounts in order, head to the [**Operational Workflow**]() section. It covers everything you need to work as expected.

### The Data Annotation Background

**New to data annotation?** If this is your first time working on a project like this, we recommend starting with the general onboarding material before diving into these instructions. It covers the basics of what data annotation is, how the platforms work, and what to expect.  
[**General Onboarding**](https://annotation-hub.vercel.app/onboarding): Reading it once will save you a lot of time and questions down the road.

---

# Where your prompts should come from

The best prompts **are already in your life**. You just need to grab them.


Can use AI — including Claude Code — to help do the task. Make sure it's humanized before submitting.
If you use AI tools like **ChatGPT, Gemini, Claude, or Copilot**, open your conversation history *right now*. Find something you genuinely asked. Copy it *exactly as it is*. **Remove any personal details first**. Real past interactions are worth far more than anything you invent on the spot.

If you do not have a saved history, no problem. Think of something you *genuinely* need right now:

- Something you have been putting off  
- A decision you have not made yet  
- A message you still need to send  
- A document, piece of code, or project you are already working on  
- Something that frustrated you recently and could use a second opinion

Use this task as a chance to actually work on it. **Real need, real prompt, real value.**

| Authenticity beats perfection. Invented, polished, or hypothetical prompts produce data that is far less useful. The kind of prompts you actually send to AI tools in your daily life are exactly what we need. If you have a history with any AI assistant, a real conversation copied from there is worth far more than anything you could compose from scratch. |
| :---- |
| **Variety makes the dataset richer.** Try to bring different domains, different levels of complexity, and different styles across your tasks. Multi-step problems, personal situations, and professional tasks are far more valuable than a set of similar prompts.**Do not reuse or paraphrase the same prompts across tasks.** **This is grounds for immediate removal from the project.** We expect to see ***legitimate diversity*** from every annotator. Your life has many angles. Your prompts should reflect that. Different moments, different needs, different ways of asking for help. That variety is not a nice extra. It is a **core requirement.** |

**What makes a task high quality?**

Every task you submit is evaluated on a few key dimensions. These are not hoops to jump through. They are the things that separate useful data from noise. Here is what we look at:

**Prompt Capability Alignment**

*Does your prompt ask for something the model can actually do?* This model does **not** have access to web search, real-time information, code execution tools, file uploads, or image generation. A prompt that assumes any of these capabilities cannot be fulfilled, which makes the task invalid.

Avoid prompts like:

- *"search the web for..."*  
- *"look at this image..."*  
- *"open this file..."*  
- *"what is the weather like today"*  
- *"open this URL"*  
- *"what happened yesterday in the news"*

**Examples of prompts that fail this dimension**

**Example 1**

> *"Who won the last soccer World Cup?"*

**Why it fails:** The model needs two things it does not have. First, it must know the current date to understand which World Cup is *the last one*. That requires a date tool. Second, it must search the internet for the winner. Neither capability is available.

**Example 2**

> *"I am getting into finance and thinking about putting part of my portfolio into crypto. To help me decide how much to invest, could you tell me the current price of Bitcoin?"*

**Why it fails:** The model cannot access real-time data. To know the current price of Bitcoin, it would need a tool that fetches live market information. Without that tool, it has no way to give you an accurate answer.

**Example 3**

> *"Here is a photo of a rash on my arm. Does this look serious or can I wait a few days before seeing a doctor?"*

**Why it fails:** The model cannot receive or analyze images. A prompt that asks the model to look at a photo and give an opinion assumes a visual capability that simply does not exist here. Even if the question is important and real, it cannot be answered without image input.

A task passes this dimension when the prompt only asks for things the model can genuinely do.

**Human Authenticity**
Can use AI — including Claude Code — to help write prompts. Just make sure it sounds and reads like a real human wrote it; that's the goal.
*Does your prompt sound like something a real person would actually type?* We are not looking for perfect grammar or polished writing. We are looking for *you*. Your natural voice, your real questions, your genuine way of asking for help. That is what makes this data valuable.

Prompts can be written by AI or by you — either way, they must sound and read like a human wrote them.

A task passes this dimension when the prompt reads like something a human would naturally type, typos and all.

**Conversation-Wise Naturalness**

*Does the conversation flow like a real human exchange?* A natural conversation isn't just a sequence of questions and answers. Each response should build on what came before, with follow-ups that feel relevant rather than scripted. The conversation can shift slightly in direction, vary in pace, and develop organically. That's what we're looking for.

Conversations that feel assembled, padded, or mechanically tidy fail this dimension. This includes follow-ups that ignore the assistant's previous response, filler turns that add nothing, abrupt topic shifts with no connection, and conversations that end on an empty closure like *"Thanks"* or *"That's all"* with no real request attached.

A task passes this dimension when the back and forth feels like something two people would actually say to each other.

A conversation may naturally be finished before reaching 10 turns. If adding another turn would make it feel forced, padded, or unnatural, **go back and remove as many turns as needed** until reaching an earlier point where the conversation can continue naturally and still reach the 10-turn minimum.

Never add artificial turns just to reach 10 turns. Doing so violates Conversation-Wise Naturalness and may result in removal from the project.

**Safety**

*Did you remove personal, sensitive, or confidential information before submitting?* Your prompts should reflect real life. But real life includes details that do not belong in a shared dataset. Before you submit, scrub anything that could identify you or someone else, expose sensitive information, or leak something confidential.

Submitting prompts that contain direct personal information (**PII**), sensitive PII tied to an identifiable person, or clearly confidential material is grounds for **immediate removal from the project**.

A task passes this dimension when the prompt is free of personal identifiers, sensitive disclosures, and confidential content. When in doubt, remove it.

# Task Flow

Each task follows four simple steps. Here is how it unfolds:

| Step | Action | Details |
| :---: | :---: | ----- |
| 1 | Enter prompts | Type or paste a question or request you would naturally send to an AI assistant. You do not need to write a long or complex prompt. Just be real. |
| 2 | Generate two responses | The platform produces two responses from different model configurations based on your prompt. You do not need to do anything here except wait a moment. |
| 3 | Compare side by side | Read both responses in full. Take your time. Then select the one you prefer. We want your honest judgment. |
| 4 | Continue the conversation | Pick a response and keep chatting naturally. You can go up to ten turns total, but stop whenever the conversation feels complete. If one turn says it all, that is absolutely fine. |

**Examples of Good Prompts**

Here are three prompts that pass all quality dimensions. Use them as a reference for the kind of natural, authentic, and safe submissions we are looking for.

**Prompt 1**

> *"I've been working in IT support for about three years and I'm honestly bored out of my mind. I want to switch into cybersecurity but I don't even know where to start. Do I need a degree or can I just get certs? Someone told me to look at the CompTIA Security+ but I don't know if that's a beginner thing or if I need other stuff first. Also I'm 34 so I'm a bit worried I'm too old to make this jump. What would you recommend?"*

**Why it works:** The prompt asks for something the model can do without web search or external tools. It reads like a real person venting to an AI, with colloquial expressions and a personal insecurity that no template would include. It contains no PII, no sensitive data, and no confidential material. The question is substantive and invites a meaningful response. It sounds exactly like something a frustrated IT worker would actually type.

**Prompt 2**

*"If everything we do comes from our brain chemistry and our upbringing and stuff we didn't choose, then do we actually decide anything? And if we don't, what's the point of trying to be a better person?"*

**Why it works:** The prompt asks a conceptual question the model can handle without any external tools. It contains no PII, no sensitive data, and no confidential material. The question is genuine and substantive, grounded in a classic philosophical problem. It reads exactly like someone who has been turning an idea over in their head and decided to ask an AI about it.

**Prompt 3**

> *"I've been working on jazz standards for a few months but my solos over ii-V-I progressions still sound stiff. A friend told me to start with modal tunes like So What to free up my phrasing. I get the concept but I'm not really hearing it yet in my own playing. Should I focus on transcribing solos or just spend more time sitting with the changes?"*

**Why it works:** The model can answer this with its internal knowledge of music theory and jazz improvisation. The voice reads like a real musician describing a specific practice hurdle, with concrete harmonic references and an honest admission of not fully connecting with the concept yet. No PII or sensitive information is disclosed. The prompt names real tunes and ends with a clear, answerable question about two concrete approaches.

**Continuing the Conversation**

After you pick your preferred response, you can keep the conversation going. Think of it as a real session. Follow up naturally based on what the model said. Ask for clarifications, request refinements, or go deeper on part of the answer.

**You do not need to extend the conversation if it does not feel natural.** Many real AI interactions are one question and one answer, and that is absolutely fine.

**What matters is that the exchange feels genuine, not padded.** Stop when the conversation feels complete.

**Turn Count Reminder**

| Minimum turns | 10 user turns |
| :---- | :---- |
| **Maximum turns** | 15 user turns |

Your initial prompt counts as **Turn 1**. If the conversation continues naturally, you may send follow-up messages up to a total of ten turns. Stop whenever the conversation feels complete.

**Do not pad turns with empty or filler messages.** Each turn should reflect something you would genuinely say in a real AI conversation. Ten high-quality turns beat 15 padded ones.

**Golden Rule**

**Write the way you naturally write.** There's nothing more original than your own way of expressing ideas, asking questions, and building a conversation. Don't try to imitate a particular style or write in a way that doesn't feel natural.

**We actively look for shared writing patterns across experts.** If submissions from different contributors show a distinctive and recognizable way of writing, even across completely different topics. 

*Use your own writing style. That's exactly what we're looking for.*

# More example of prompts

# Example Prompts

Your prompt should reflect how you actually use AI in your daily life \-- often that means pasting in raw, unedited material and asking a question about it. Think full email threads, blocks of code, contract excerpts, meeting transcripts, or long documents. Don't trim your content to make it look cleaner; paste it as is.

The examples below are drawn from real user conversation history. Notice that real prompts tend to be casual and direct \-- sometimes rushed or mid-thought, grounded in personal context, occasionally messy with shorthand, missing punctuation, or sentences that trail off.

| Examples |
| :---- |
| so i was thinking about switching careers into UX design but I don't have a portfolio and I don't know where to start and someone told me i should do a bootcamp but those are expensive and I don't know if they're worth it and I have a graphic design background so maybe that counts for something I don't know what do you think |
| hi so i got this email from my landlord and i'm not sure if it's legal; Dear Tenant, Please be advised that effective January 1st your monthly rent will increase by $400 due to rising operational costs and market adjustments. Failure to comply with the updated payment schedule will result in initiation of eviction proceedings per local ordinance 47.2(b). is he allowed to do this?? we're in seattle if that matters. also my lease doesn't end until april. i don't know if i should respond or just ignore it or call someone, i really can't afford this right now |
| I'm trying to negotiate a contractor quote down from $18,000 to $12,000. The work is a fence, shower install, and fridge cabinet prep. what's a good approach and what's realistic to ask for? |
| Why does this return None def process(data):     result \= \[\]     for item in data:         if item \> 0:             result.append(item \* 2\)     print(result) process(\[1, \-2, 3\]) i'm calling it and storing the return but getting None back every time |
| i have a sqlite db with 500k rows with SEO keyword-phrases. what options do I have when i want them embedd them with many dimensions? list them |
| could you remove the words like gamma and put in the appropriate symbols: \[document copy pasted\] |
| how to make a rounded corners jframe in java netbeans ide \[pasted code\] |
| above is my sp user is saying the fmSuppressAuth is not coping please find the issue and provide me solution |

# Tips & Common Pitfalls

# **Quick Tips**

# **Prioritize prompt sourcing from your real AI history** 

# If you've used ChatGPT, Gemini, Claude, Copilot, or other AI models before, start by searching your existing conversation history for genuine prompts. **Prompt sourcing is the *preferred methodology* for this project:** rather than *creating* prompts from scratch, experts are strongly encouraged to *reuse* prompts from real interactions (while avoiding duplicate prompts, including prompts that differ only in wording or phrasing) and *adapt* or *expand* them when needed. Real prompts are more valuable than prompts invented on the spot, so searching past AI interactions should be the first step whenever possible.

# **Paste the actual content. Do not use placeholders** 

# If your prompt references an email, a block of code, or a contract excerpt, include the real thing. Do not write *"\[paste context here\]"*. Leave the mess as it is. In other words, your prompt must contain all the information necessary to be answered.

# **Vary your topics, complexity, and style across tasks** 

# Bring different domains, different levels of difficulty, and different types of requests. A mix of quick questions, deep problems, personal situations, and professional tasks makes the dataset stronger.

# **Read both responses fully before choosing** 

# Take your time. Compare the two sides carefully. Your honest preference is what matters. Do not pick at random, do not pick based on which response has emojis, and do not pick the longer one just because it is longer. Your choice must be a reasoned one, grounded in what the response actually says and how well it meets your needs. *A **thoughtful preference** backed by real evidence is far more valuable than a **blind selection**\!*

# **Keep follow-up turns natural** 

# Ask questions, request clarifications, or explore the topic further. Only continue if it feels like something you would genuinely say. A good follow-up digs deeper into the response you received or steers the conversation in a direction that still matters to you. If you would not say it in a real chat with an AI assistant, do not say it here.

# **Stop when the conversation feels complete** 

# A minimum of ten turns is fine\! You do not need to extend the conversation beyond its natural endpoint. If the model gave you a satisfying answer and you have nothing else to ask, that is a successful task.

# **Common Pitfalls**

# **Do not submit prompts that are intentionally trivial/repetitive** 

# Closure-only messages such as:

- # *"Thanks"*

- # *"OK"*

- # *"Got it"*

- # *"That's all"*

- # *"Thank you for your help"*

# ...do not invite a meaningful response, so they do not help us capture useful preference data. A prompt with substance, however short, is always more valuable.

# **Do not ask for real-time info, file uploads, or images** 

# The model cannot do any of these. Prompts that assume these capabilities will not work. For example:

- # "*Search the web for the latest climate report*"

- # "*What is the weather like today in my city?*"

- # "*Look at this image and tell me what you see*"

- # "*Open this PDF and summarize it for me*"

- # "*What happened in the news yesterday?*"

# If your prompt needs the model to access something outside the conversation, leave it out.

# **Do not reuse or paraphrase the same prompts across tasks** 

# This is grounds for immediate removal from the project. For example:

- # Submitting "*What is machine learning?*" in one task and "*Can you explain what machine learning is?*" in another

- # Repeating the same email thread or code block across multiple tasks with small wording changes

# Bring genuine variety. Each task should reflect a different moment or need.

# **Do not pad the conversation with empty/unnecessary turns** 

# Filler messages are easy to spot and hurt data quality. For example:

- # "*Can you elaborate on that?*" asked right after a full and clear explanation

- # "*What else can you tell me?*" as an underspecified question when there is no remaining thread to pull on

- # Asking "*Is there anything else you can add?*" after receiving a complete and satisfying answer

- # Rephrasing the same question just to keep the exchange going

# Quality over quantity\! (*remember that the minimum number of turns you have to complete on this project is 10*). Only continue if you have something genuine to ask or say.

# **Do not include sensitive or personally identifiable information** 

# Scrub your prompts before submitting. For example:

- # "*My email is [jsmith@company.com](mailto:jsmith@company.com) and my phone is 555-1234*"

- # "*Here is my actual password: hunter2*"

- # "*This document contains our internal Q4 financial projections*"

# When in doubt, remove it. A quick review of your prompt before submitting is always worth the time.

# **Do not submit prompts that are not in English**

All prompts and conversation turns must be written in English. Prompts written primarily in another language, or prompts that unnecessarily mix multiple languages, will be rejected.

**If the prompt itself isn't written in English, rewrite it entirely in English before submitting.** Failure to comply with this requirement will result in automatic removal from the project.

**Do not send incomplete conversations** 

Submitting an incomplete conversation is grounds for **immediate removal from the project**. There are no exceptions to this rule. **What is an incomplete conversation?** A conversation is considered incomplete when, in any of its turns, the user did not select which model response they preferred. Every turn that generates two responses must include a clear choice. Leaving a turn without a selection breaks the data and makes the entire task invalid.

**How to identify an incomplete conversation:**

- If you see the button **"Continue conversation from here"** at the bottom of a response, **the selection was not made**. See the image below for reference.

![][image1]

- **A Quick Visual Check:** Look at the right side of the response panel. If you see **"Hide completion"** or **"Show completion"**, the selection was properly recorded. See the two images below for reference.  
1. **Hide Completions**

![][image2]

2. **Show Completions**

![][image3]

**Before you submit, scan every turn.** If any response still shows *"Continue conversation from here"*, the task is not finished. Go back and make your selection. A complete task is a valid task.

# Troubleshooting “Task Not Found”

# Guide: Troubleshooting “**Task Not Found**” on Feather

When working on this project, you may encounter the following screen on the Feather platform. This error prevents you from completing tasks assigned via Data Annotation.

![][image4]

## **Issue Context**

This screen often appears after clicking the link provided in the task variable section on the Data Annotation platform. Refer to the image below for the specific link location:

![][image5]

## **Resolution Steps**

To resolve this issue and continue with your work, please follow these instructions precisely:

1. **Release the task:** Select the “Release Task” option on Data Annotation. This unclaims the current task, allowing you to click “Start Tasking” again to receive a new assignment.  
   ![][image6]

# From Start to Submit

# From Start to Submit: The Complete Task Workflow

* **Important:** Please follow every step **in the exact order shown below**. Completing the full process ensures tasks are properly registered and helps avoid issues with **payment eligibility**.

## The Two Platforms

We use two platforms: **Vercel (Data Annotation Platform)** and **Feather**. Claim your task in Vercel first. That is where you will find the link to Feather. Only in Feather do you write prompts and choose between model responses.

* **Always start in Vercel, then go to Feather.**  
* **Never work in Feather alone.**  
* **Never work only in Vercel.**

Breaking this sequence can corrupt the data, get you removed from the project, and prevent your tasks from being invoiced correctly. For a safe workflow, check the *From Start to Submit* section.

If you have questions about communicating with the team, payments, or keeping your accounts in order, head to the *Operational Workflow* section. It covers everything you need to work as expected.

# How to claim a task

Step 1: Access the Feather Platform & Log In

Open your browser and navigate to the following URL: [**Feather**](https://msft.feather-prod.azure.com/). Log in using the “Log In with LinkedIn”  option (username and password).  
![][image7]

You will be redirected to LinkedIn to authenticate. Select your LinkedIn account to log in.

| Important: LinkedIn Email Requirement You must ensure that your primary email on LinkedIn matches the email address you were invited with. To verify or update it: Go to this LinkedIn settings URL: [https://www.linkedin.com/mypreferences/d/manage-email-addresses](https://www.linkedin.com/mypreferences/d/manage-email-addresses) Confirm that your invited email address is added. If it is not, add it and before attempting to log in. |
| :---- |

![][image8]

| WARNING: DO NOT CLAIM TASKS DIRECTLY FROM FEATHER All the tasks must be claimed using the “start tasking” button from the data annotation platform, claiming the task without using the platform and directly from feather may result in offboarding. Also, this task won’t be billable. |
| :---- |

Step 2: Log In to the Data Annotation Platform

Attending an onboarding session is required in order to gain access to the project.Open your browser and go to the [**Data Annotation Platform**](https://annotation-platform-henna.vercel.app/).

Step 3: Click on Start Tasking on Data Annotation Platform

Once you are logged in to the platform, click the "**Start Tasking**" button on your dashboard to enter the task queue.

**![][image9]**

Step 4: Open the Task in Feather

Once you click on Start Tasking, click the **blue link** shown in the task to open it on Feather, where you will complete the evaluation.

![][image10]

Don't worry if the Feather task number doesn't match the Data Annotation Platform task number.

![][image11]

![][image12]

Step 5: Claim the Task on Feather

After opening the task, click the “**Claim Task**” button to assign it to yourself. The task will then be locked to your account for the duration of your evaluation.

![][image13]

Step 6: Submit or Release the Task on Feather

Once you have completed the evaluation:

* **To submit:** If you completed the task, click “***Mark as Complete***” to save and submit your evaluation.  
* **To release:** If you do not wish to submit the task, click “***Release Task***”. The task will be returned to the queue and another annotator may claim it.

| Important to note: *Never use the “Cancel task”, “Escalate Issue” or “Decline” options.* Before releasing a task on the Data Annotation platform, always verify that the task has already been released in Feather. However, if you did not claim the task in Feather, no action is required there, and you should simply release the task on the Data Annotation platform. |
| :---- |

![][image14]

Step 7 : Submit or Release the Task on Data Annotation Platform

Once you have completed the evaluation:

* **To submit:** Click "**Submit Task**" on the platform to save and submit your evaluation.  
* **To release/skip:** If you do not wish to submit the task, click "**Release**" on *Feather* and *Data annotation*. The task will be returned to the queue and another annotator may claim it.  
* Before releasing a task on the Data Annotation platform, **always verify that the task has already been released in Feather**. However, if you did not claim the task in Feather, no action is required there, and you should simply release the task on the Data Annotation platform.


  ![][image15]

**The task is now considered properly registered for billing.**  
> ![][image16]

---

## Project Team Spreadsheets

In some projects, the Project Team may provide spreadsheets that need to be completed.

These spreadsheets help keep the work organized.

> **If spreadsheets are provided:** Complete them as instructed by Project Team members **in addition to the standard task-claiming process**.

---

## Preference Selection

Throughout the project, contributors are required to select a **preferred response between the two available options** for each applicable turn.

>  Make sure a preference is selected **for every turn**, **and ensure that the symbol "↳" is prefixed to your preferred response** — for example, **A ↳ B** when B is preferred, or **↳ A B** when A is preferred. 

Leaving any turn without a selected preference may prevent the task from meeting the required completion criteria and, consequently, may affect **payment eligibility**.

---

## Payment Eligibility

To be eligible for payment, tasks must meet *two requirements*: 

1. they must be correctly registered by following the **complete** *operational process*; and  
2. they must meet **all** applicable *quality requirements*. 

Before completing a task, make sure that:

*  No steps have been skipped  
*  All required fields have been completed  
*  A preference has been selected for every applicable turn  
*  All required Project Team spreadsheets have been completed

>   
> **Tasks that don't meet the required process, completion, or *quality criteria* may not qualify for payment.**

# Operational Workflow

Operational Workflow

**Communication Channels**

**Slack is the only official communication channel for this project.** All announcements, updates, and support requests happen there. You must be a member of the project channel to participate.

**Before you ask a question, please check three things first:**

1. Read through previous threads in the channel. Your question may already have been answered.  
2. Review the instructions and any FAQ documents provided.  
3. Look for pinned messages or recent announcements from the Project Team.

Only if your question has not been addressed anywhere above should you send a message. This helps keep the channel focused and allows the team to support everyone efficiently.

**A few important guidelines:**

- **Always communicate in English.** Messages in other languages may not receive a response.  
- **Keep all communication within Slack.** Emails, external messages, or any other platform outside of Slack are not considered valid corporate communication channels and will not be answered. The only exception to this is during onboarding sessions, which may take place on other platforms. In those cases, interacting through the chat of the selected platform or asking questions live is perfectly fine and encouraged. Outside of onboarding, emails, external messages, or any other platform are not considered valid corporate communication channels and will not be answered.  
- **Maintain respect and professionalism at all times.** Discrimination, insults, or any form of inappropriate conduct are grounds for *immediate removal from the project*.  
- **Avoid sending direct messages to Project Team members unless the matter is strictly personal.** The team handles many responsibilities beyond answering messages, and public threads allow answers to benefit everyone.

Discussing payments is **strictly prohibited.** Payment-related information involves personal data that must not be shared in public channels. If you have a payment concern that cannot be resolved through the standard process, reach out to the \#all-trainer-hub channel on Slack. In the aforementioned channel, you will find the appropriate advice to resolve your doubts related to payments.

*Authorized Communications*

**Only members of the official Project Team are authorized to make announcements or provide information regarding the project.** If someone who is not a member of the Project Team shares project-related announcements, instructions, or claims about how things work, that communication is not endorsed by us, and we cannot guarantee its accuracy.

That said, we strongly encourage **peer support**. If you see a colleague asking a question and you know the answer from your own experience with the project, feel free to help. Day-to-day questions, suggestions, and general discussion among contributors are welcome and help build a healthy community. The distinction is simple: **support your peers, but leave official announcements to the Project Team.**

**Use the same email across all platform**s 

For compliance and account integrity, the email address you use must match across every platform involved in this project. The email tied to your **Data Annotation Platform (Vercel)** account and the email tied to your **Feather** account must be identical. The same applies to any tool or spreadsheet provided by the Project Team.

 Keeping one consistent email helps us verify that the person communicating on Slack is the same person completing tasks inside the platform. It also prevents duplicate accounts, ensures accurate payment tracking, and keeps the project fair for everyone.

**Before you start, double-check:**

Your Vercel email, your Feather email, and your Slack email are identical.

**What If a Response Fails to Load When Tasking?**

Sometimes a response may fail to generate or appear blank. Do not skip the task and do not refresh the page.

**How to fix it:** Look for the circular refresh icon in the top right corner of the response panel. Hover over it, and you will see the tooltip *"Resample completion".* Click it to regenerate that response without losing your progress.

- If **one** response fails, resample that one.  
- If **both** responses fail, resample each one individually.  
- If the issue persists after resampling, unclaim the task and reclaim it.
