if ["$1" == ""] || [$# -eq 0]; then
    echo "Python version is needed - ./buildlambda.sh 3.6"
else
    echo "Creating layer compatible with Python $1"
    docker run -v "$PWD":/var/task "lambci/lambda:build-python$1" /bin/sh -c "pip install -r requirements.txt -t python/lib/python$1/site-packages/; exit"
    zip -r layer.zip python > /dev/null
    rm -r python
	echo "Layer was successfully created"
	ls -lah layer.zip
fi