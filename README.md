# taskMonitor
>Manages the progress of program on your cloud computer, and provides a simple UI via HTTP.
***
This is a python project that displays your task progress on a cloud computer or infrastructure.
Your task program can update its progress via UDP using the api provided (or you can implement it your self).
Then the server provides a UI via HTTP and HTML.

***
###Technical Info:
+ This project is in a rudimentary stage. It can run well on most circumstances, but has **no guarantee** of performance, especially on **security** aspects.
Therefore, it is recommended to be used inside a firewall and only monitor trusted programs.

+ The templating system in the server is just a simple implementation using string format. It is not suitable for too complex tasks.

***
This project is part of [LTW](https://ltw-tech.top) infrastructure.