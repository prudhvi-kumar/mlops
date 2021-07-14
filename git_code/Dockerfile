FROM Centos:latest
RUN yum install python36 -y
RUN pip3 install numpy
RUN pip3 install joblib
RUN pip3 install scikit-learn
COPY "marks secured.pk1" /
COPY prediction_using_joblib.py /
