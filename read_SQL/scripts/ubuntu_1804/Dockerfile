FROM ubuntu:18.04

RUN apt-get update\
 && apt-get install -y --no-install-recommends\
 g++\
 make\
 cmake\
 omniorb-nameserver\
 python-omniorb-omg\
 omniidl-python\
 doxygen\
 nkf\
 gnupg2\
 python\
 && export repo="http://openrtm.org/pub/Linux/ubuntu/ bionic"\
 && echo "deb $repo main" | tee -a /etc/apt/sources.list\
 && apt-key adv --keyserver keys.gnupg.net --recv-keys 4BCE106E087AFAC0\
 && apt-get autoclean\
 && apt-get -qq update\
 && apt-get install -y --force-yes openrtm-aist-python openrtm-aist\
 && apt-get clean\
 && rm -rf /var/lib/apt/lists/*

COPY read_SQL /root/read_SQL
WORKDIR /root/read_SQL
RUN mkdir build && cd build && cmake .. -DBUILD_DOCUMENTATION=ON -DBUILD_TESTS=ON && make && make doc && make install && cpack\
          && export CTEST_OUTPUT_ON_FAILURE=1 && make test
