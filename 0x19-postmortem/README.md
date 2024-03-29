# postmortem

## Tasks
### Summary

From 5:00 AM to 6:50 PM GMT, reuests to Holberton API hosted on [0x17-web_stack_debugging_3](../0x17-web_stack_debugging_3) sandbox resulted in 500 error response messages. Any applications that rely on this API returned errors or had reduced functionality. At its peak, the issue affected 100% of traffic to this API infrastructure. The root cause of this outage was a typing mistake in configuration files that caused to API to malfunction.

### Timeline (all GMT)

* 4:45 AM: Configuration push behins
* 4:46 AM: Outage begins
* 5:00 AM: Pagers alerted teams(Alx released [0x17-web_stack_debugging_3](../0x17-web_stack_debugging_3))
* 6:30 PM: Check status of Aache2(running)
* 6:40 PM: Check PHP configuration files and fix wp-settings.php
* 6:49 PM: Server restarts begin
* 6:50 PM: 100% of traffic back online

### Root Cause & Resolution
#### Resolution

At 5:45 AM GMT, a configuration change was inadvertently released to our production environment without first being released to the testing environment. The change in wp-settings.php included a typo of .phpp instead of php on one of the lines. This problem caused Apache to return 500 error anytime that PHP website is hit. The configuration error quickly caused all the serving threads to be consumed. TRaffic was permanently queued waiting for a serving thread to become available. The servers becan repeatedly hanging and restarting as they attempted to recover and at 5:46 AM GMT, the service outage began.

#### Resolution

At 5:00 AM GMT, the monitoring systems alerted our engineers who investigated and escalated the issue. By 6:40: PM, the incident response team identified that the monitoring system was exacerbating the problem caused by this typo.

At 6:30 PM, we attempted to restart Apache2 and it was running alrigh. This made us check server logs with ltrace to discover the typo in php configuration files. Since the file was big we could not risk fixing only one line and leaving potential other typos. So we used puppet script to replace any occurence of the typo in the entire file with the right word.

The jobs started to slowly recover, and we determined the overall recovery would be faster by a resatrt of the API infrastructure. By 6:49PM, 90% of traffix was restored and 100% of traffic was routed to the API infrastructure at 6:50 PM.

### Corrective & Preventive Measures

In the last hours, we've conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and avoid repeating same mistakes:
* Disable the current configuration release mechanism untill safer measures are implemented.
* Change rollback process to be quicker and more robust.
* Fix all typos in configuration files before deploying.
* Programatically enforce staged rollouts of all configuration changes.
* Improve process for auditing all high-risk configuration options.

![Screenshot from 2023-08-08 20-08-30](https://github.com/samuelselasi/alx-system_engineering-devops/assets/85158665/4881937f-2b1d-4809-9d86-4296739e4ced)
