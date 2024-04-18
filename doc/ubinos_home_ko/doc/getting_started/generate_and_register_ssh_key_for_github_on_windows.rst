윈도우에서 깃허브용 SSH key 생성 및 등록하기
-------------------------------------------------------------------------------

다음은 윈도우 10 64비트 버전에서 깃허브용 SSH Key를 생성하고 등록하는 과정을 설명한다.

SSH key를 생성하고, 깃허브 사이트를 known_hosts로 등록하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 명령어 프롬프트 "cmd"를 연다.

2. 다음 명령을 입력해 SSH key를 생성한다.

    .. code-block:: console

        ssh-keygen -t rsa

3. 다음 명령을 입력해 깃허브 사이트를 known_hosts로 등록한다.

    .. code-block:: console

        ssh-keyscan -t rsa github.com >> "%USERPROFILE%\.ssh\known_hosts"

윈도우 홈의 SSH 구성 파일들을 MSYS2 홈으로 복사하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. "윈도우키 + R키"를 누른 후 "MSYS2 UCRT64"를 입력하고 엔터키를 눌러 MSYS2를 연다.

2. 다음 명령을 입력해 윈도우즈 홈의 SSH 구성 파일들을 MSYS2 홈으로 복사한다.

    .. code-block:: console

        cp -a "$USERPROFILE/.ssh" ~/

SSH Key를 깃허브에 등록하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. "윈도우키 + R키"를 누른 후, "Git GUI"를 입력하고 엔터키를 눌러 Git GUI를 연다. 그리고 Menu --> Help --> Show SSH Key를 선택해 생성된 키를 확인 한 후, "Copy to Clipboard" 버튼을 눌러 SSH key를 클립보드로 복사한다.

2. 다음 깃허브 웹사이트 에 접속해 로그인 한 후, 우측 상단 아이콘 --> Settings --> SSH and GPG Keys --> New SSH Key 를 선택한다.

    * `<https://github.com>`_

3. Add new SSH Key 웹페이지가 열리면 키 입력 텍스트 박스를 클릭한 후 "Control + V키"를 눌러 SSH key를 붙여넣는다.

4. Key name은 자유롭게 입력하고, Key type으로 "Authentication Key"를 선택한 후 "Add SSH Key" 버튼을 누른다.
