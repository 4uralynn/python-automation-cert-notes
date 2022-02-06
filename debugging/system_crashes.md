Crashes in Complex Systems
==========================

Complex system crashes require an undersatdning of ***how various machines interact***. It will be
important to **find any logs specific to the failing service** as well as **general system logs**.
It is to **understand any changes to the system**, using *version control like Git*. 

Whenever possible, the best strategy is to **rollback the changes** that you suspect are causing 
the issue. If the system allows for easy rollbacks, this will quickly get the system back in 
working shape while you diagnose the issue. **It will also** ***eliminate*** **that change as a**
**possible cause to the crash**.

**When comming across unhelpful error messages**, take a moment to **improve vague error messages**.
Then it will help you diagnose other issues in the future.

**It is important to be able to quickly deploy new machines when necessary.** If rollbacks don't
fix the situation, you may need to remove the affected server from the pool and spin up a new server.
This can be accomplished by keeping ***stand-by servers***, in case you need them; or having a 
tested pipeline for deploying new servers on demand. Many companies now deploy virtual machines 
in the cloud.

  + For the cloud, there may be limits set by third-parties as to bandwidth, storage, etc. 


## Communication and Documentation of Incidents

You may do a great job fixing the issue, but **if you do not communicate what is going on during**
**the process, you may have a bunch of frustrated users**. You could also end up skipping important
steps, forgetting vital details, and wasting a lot of time if you don't **write down your progress**
**while solving a problem**. Documenting what you do lets you **keep track of what you've tried and**
**what the results were**.

It is important to **communicate clearly witht those affected by the issue**:

  + What you've figured out.
  + Available work-arounds (what they can expect as a solution)
  + When they can expect the next update
  + Timing
  + Delegation (who else is involved)

The more people affected, the more regular updates you want to give **so users can plan and**
**organize their time**.

If more people are involved in finding the solution, **agree on who is going to work on which**
**tasks**. 
  
  + You want to ***designate a person who is incharge of communicating to users***
    - Often called the **Communications Lead**
  + Also designate ***another person deligating the different tasks to the team membners***. 
    - Sometimes called the **Incident Controller** or **Incident Commander**

When the issue is resolved, **a summary should be written**, including:

  + The *root cause*
  + The *process of diagnosing the problem* and finding that cause.
  + *What fix you implemented* to resolve the issue.
  + *Long term remediation*, so the problem doesn't happen again.

## Postmordems

Documents that *describe details of incidents to help us learn* from our mistakes are called
**postmortems**.

The goal is to *learn from what happened in order to avoid it happening again*. You want to
communicate aspects that help in *learning from the issue*:

  + What caused the issue?
  + What was the impact of the issue?
  + How was the issue diagnosed?
  + What parts *went well*?
  + What short-term remediation was applied?
  + What long-term remediation is recommended?

If the postmortem is long, include a summary that specifically highlights, the **cause**, **impact**,
and the **long-term remediation recommendations**. 

