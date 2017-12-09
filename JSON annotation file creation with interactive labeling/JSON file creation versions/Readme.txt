This folder contains the older method that I tried to produce json file.

Older Approach:
Creating annotation file and labeling side by side.

Problem:
If I leave creation of annotation file after labeling and termination of loop, it was risky.
Why risky?
Because maybe lets say I have labeled 600 images, but due to exception or powert outage my program is terminated. Then what? All things lossed. Frustrating. Right?

so lets write in annotation file in the loop while labeling each time. BUT
If I append in annotation file each time:
As values of some keys(objects) are not going to change with every loop iteration, so appending in annotation file each time produces redundant data violating the desired format.

If I delete these keys or make different dictionary variables, it results in violation of desired annotation format.
