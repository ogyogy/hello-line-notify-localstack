include .env

deploy: my-deployment-package.zip
	awslocal lambda create-function \
		--function-name hello-line-notify-function \
		--runtime python3.9 \
		--zip-file fileb://my-deployment-package.zip \
		--handler lambda_function.lambda_handler \
		--role cool-stacklifter
	awslocal lambda update-function-configuration --function-name hello-line-notify-function \
    	--environment "Variables={LINE_NOTIFY_ACCESS_TOKEN=${LINE_NOTIFY_ACCESS_TOKEN}}"
	awslocal lambda create-function-url-config \
		--function-name hello-line-notify-function \
		--auth-type NONE

my-deployment-package.zip: package
	cd package/ \
		&& zip -r ../my-deployment-package.zip . \
		&& cd ../ \
		&& zip -g my-deployment-package.zip lambda_function.py

package: lambda_function.py
	pip install --target ./package requests

clean:
	rm -rf ./package
	rm -f my-deployment-package.zip
	-awslocal lambda delete-function-url-config --function-name hello-line-notify-function
	-awslocal lambda delete-function --function-name hello-line-notify-function