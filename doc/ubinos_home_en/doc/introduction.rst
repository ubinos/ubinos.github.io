.. _introduction:

*******************************************************************************
Introduction
*******************************************************************************

Ubinos(Ubiquitous Computing Network Operating System) is an operating system designed and implemented to fit the ultra-small and ultra-low-power terminal equipment of ubiquitous computing(IoT) networks.

The design goals are as follows:

* Suitable for ultra-small and ultra-low-power device development
* Suitable for application development that simultaneously performs sensing, control, and communication
* Suitable for physical device control application development

Ubinos has been designed and implemented to achieve these goals with the following features:

* Features for ultra-small and ultra-low-power device development
    + Small RAM and ROM memory usage
    + Small power consumption
    + Support tickless idle
* Features for application development that simultaneously performs sensing, control, and communication
    + Support multitasking
    + Support various communication functions between tasks
        - Semaphore, mutex, message queue, condition variable
        - Can wait for multiple signals(semaphore, mutex, ...) simultaneously
* Features for physical device control application development
    * Support features for real-time response guarantee
        - Priority-based preemptive round-robin scheduling feature
        - Priority inheritance for preventing priority inversion

The following figure shows the Ubinos architecture.

.. image:: /_static/image/ubinos_architecture.png
    :width: 800 px
    :align: center
    :alt: Ubinos architecture

.. centered::
    Ubinos architecture
