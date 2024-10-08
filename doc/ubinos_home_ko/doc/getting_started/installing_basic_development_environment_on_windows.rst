윈도우에 기본 개발 환경 설치하기
-------------------------------------------------------------------------------

다음은 윈도우 10 64비트 버전에 유비노스 개발 환경을 설정하는 과정을 설명한다.
사용된 설치 패키지는 2024년 2월 28일의 최신 안정 버전이다.
**언급하지 않은 설치 선택 사항은 기본 값을 사용한다.**

씨메이크(CMake) 설치하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 다음 웹사이트에서 설치 패키지를 받아서 설치한다.

    * `<https://cmake.org>`_

        + --> Download

            - --> cmake-3.29.0-rc2-windows-x86_64.msi

    * **설치 시 지정해야 하는 선택 사항은 아래와 같다.**

        + Add CMake to the system PATH for all users: **Check**

깃(Git) 설치하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 다음 웹사이트에서 설치 패키지를 받아서 설치한다.
    * `<https://git-scm.com>`_

        + --> Download for Windows --> Click here to download the latest 64-bit version

            - --> Git-2.44.0-64-bit.exe

파이썬(Python) 설치하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 다음 웹사이트에서 설치 패키지를 받아서 설치한다.

    * `<https://python.org>`_

        + --> Downloads --> Download Python 3.10.11

            - --> python-3.10.11-amd64.exe

    * **설치 시 지정해야 하는 선택 사항은 아래와 같다.**

        + Add Python 3.10 to PATH: **Check**

2. 명령어 프롬프트 "cmd"를 연 후, 다음 명령을 입력해 ttkwidgets, virtualenv를 설치한다.

    .. code-block:: console

        pip install ttkwidgets virtualenv

그누 암 임베디드 툴체인(GNU ARM Embedded Toolchain) 설치하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 다음 웹사이트에서 설치 패키지(gcc-arm-none-eabi-10.3-2021.10)를 받아서 설치한다.

    * `<https://developer.arm.com/downloads/-/gnu-rm>`_

        + --> gcc-arm-none-eabi-10.3-2021.10-win32.exe

    * **설치 시 지정해야 하는 선택 사항은 아래와 같다.**

        + Add path to environment variable: **Check**

엠시스2(MSYS2) 설치하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 다음 웹사이트에서 설치 패키지를 받아서 설치한다.

    * `<http://www.msys2.org>`_

        + --> msys2-x86_64-20240113.exe

2. "윈도우키 + R키"를 누른 후 "sysdm.cpl"를 입력하고 엔터키를 눌러 시스템 속성을 연다. 그 다음 아래 위치에 있는 **사용자 환경 변수** "PATH"의 마지막 부분에 "usr\bin"과 "ucrt64\bin" 경로를 추가한다.

    * 고급(Advanced) --> 환경 변수(Environment Variables ) --> **사용자 변수(User variables)** --> Path

        + "usr\bin" 경로 예

            .. code-block:: console

                C:\msys64\usr\bin

        + "ucrt64\bin" 경로 예

            .. code-block:: console

                C:\msys64\ucrt64\bin

3. 명령어 프롬프트 "cmd"를 연 후, 다음 명령을 입력해 기본 개발 환경 패키지들을 설치한다.
(Path 변경 사항은 변경 후 연 "cmd" 부터 반영되므로, Path 설정 후에 연 "cmd"를 사용해야 하며, 설치 중 화면이 장기간 갱신되지 않는 경우 엔터키를 눌러준다.)

    .. code-block:: console

        pacman -S --needed base-devel git openssh mingw-w64-ucrt-x86_64-toolchain mingw-w64-ucrt-x86_64-ccache mingw-w64-ucrt-x86_64-poppler

큐이엠유(QEMU) 설치하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 명령어 프롬프트 "cmd"를 연 후, 다음 명령을 입력해 QEMU 패키지를 설치한다.
    
    .. code-block:: console

        pacman -S --needed mingw-w64-ucrt-x86_64-qemu

브이에스코드(VSCode) 설치하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 다음 웹사이트에서 설치 패키지를 받아서 설치한다.

    * `<https://code.visualstudio.com>`_

        + --> Download --> ...

2. 브이에스코드를 실행 시킨 후 다음 확장 프로그램(Extension)들을 설치한다.

    * C/C++ (by Microsoft)
    * C/C++ Themes (by Microsoft)
    * C/C++ Extension Pack (by Microsoft)
    * Python (by Microsoft)
    * CodeLLDB (by Vadim Chugunov)
    * CMake (by twxs)
    * MemoryView (by mcu-debug)
    * ARM Assembly (by dan-c-underwood)
    * Hex Editor (by Microsoft)
    * Open (by sandcastle)
    * CMake Tools (by Microsoft)
    * Makefile Tools (by Microsoft)

3. 다음 확장 프로그램(Extension)들을 비활성화(disable) 시킨다.

    * CMake Tools (by Microsoft)
    * Makefile Tools (by Microsoft)

개발환경이 정상적으로 설치되었는지 확인하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. "윈도우키 + R키"를 누른 후 "sysdm.cpl"를 입력하고 엔터키를 눌러 시스템 속성을 연다. 그 다음 아래 위치에 있는 **사용자 환경 변수** "PATH"를 연다.

    * 고급(Advanced) --> 환경 변수(Environment Variables ) --> **사용자 변수(User variables)**

        + --> Path

2. 아래 그림과 같이 GNU Arm Embedded Toolchain, Python, MicrosoftVS Code, msys64 경로가 모두 추가되어 있고, msys64의 경로는 마지막에 위치해 있는지 확인한다.

.. image:: /_static/image/windows10_user_environment_variables.png
    :width: 600 px
    :align: center
    :alt: 윈도우 사용자 환경 변수

.. centered::
    윈도우 사용자 환경 변수

3. "윈도우키 + R키"를 누른 후 "sysdm.cpl"를 입력하고 엔터키를 눌러 시스템 속성을 연다. 그 다음 아래 위치에 있는 **시스템 환경 변수** "PATH"를 연다.

    * 고급(Advanced) --> 환경 변수(Environment Variables ) --> **시스템 변수(User variables)**

        + --> Path

4. 아래 그림과 같이 Git, CMake 경로가 모두 추가되어 있는지 확인한다. (이곳에 msys64의 경로가 추가되어 있으면 안 된다.)

.. image:: /_static/image/windows10_system_environment_variables.png
    :width: 600 px
    :align: center
    :alt: 윈도우 시스템 환경 변수

.. centered::
    윈도우 시스템 환경 변수

5. 명령어 프롬프트 "cmd"를 연 후, 다음 명령을 입력해 개발 도구들이 정상적으로 설치되었는지 확인한다.

    .. code-block:: console

        pip list | grep ttkwidgets
        which python
        which cmake
        which make
        which git
        which arm-none-eabi-gcc
        which ssh
        which ssh-keygen

아래는 정상적으로 설치되었을 경우 결과 예이다.

.. image:: /_static/image/windows10_installation_check_result.png
    :width: 700 px
    :align: center
    :alt: 윈도우용 개발 도구 설치 확인 결과 예

.. centered::
    윈도우용 개발 도구 설치 확인 결과 예

