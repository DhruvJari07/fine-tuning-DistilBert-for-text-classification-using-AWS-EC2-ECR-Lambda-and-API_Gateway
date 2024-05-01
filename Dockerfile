FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt  .
RUN  python -m pip install --upgrade pip
RUN  yum install gcc -y
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"


# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

COPY model_state_dict_5.pth /opt/ml/model_state_dict_5.pth

#COPY . ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.lambda_handler"]