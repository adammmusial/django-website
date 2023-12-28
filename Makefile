build:
	docker build --force-rm ${options} -t personal-website:latest .

build-prod:
	${MAKE} build options="--target production"