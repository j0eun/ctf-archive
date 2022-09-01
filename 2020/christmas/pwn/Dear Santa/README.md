올해도 어김없이 아이들에게 선물을 나눠주기 위해 한국에 입국한 산타할아버지는 큰 난관을 만나고 말았다.
그것은 바로 2주간 자가격리 기간을 가져야 한다는 것인데…!!
아이들을 만나지 못해 상심이 크신 산타할아버지를 위해 문안편지를 써 드리도록 하자.
편지 내용이 마음에 드신다면 특별한 선물이 있을 수도…?


--- Description ---
본 문제는 Open-source 온라인 FPS 게임인 Assault Cube를 활용한 프로그램입니다.

Assault Cube Github : https://github.com/assaultcube/AC

Assault Cube는 다음과 같이 환경을 구성할 수 있습니다.

$ sudo apt-get install -y libsdl1.2debian libsdl-image1.2 zlib1g libogg0 libvorbis0a libopenal1 libcurl4 libsdl1.2-dev
$ sudo apt install -y gcc-multilib clang
$ git clone https://github.com/assaultcube/AC
$ cd AC
$ git reset —hard 05003f9238a22a646773916b0b03986ada7b7eb8
$ patch -p1 < …/patch.patch
$ cd source/src
$ make install

문제 서버 접속은 main menu -> Multiplayer -> Custom connect 에서 진행할 수 있습니다.

서버 환경은 Ubuntu 18.04 LTS 이며, 서버는 1분마다 초기화됩니다.

서버를 exploit 하거나, /home/prob/flag 에 존재하는 플래그를 읽어보세요!