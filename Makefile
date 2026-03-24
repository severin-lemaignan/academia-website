
all:
	zola build
	cd public && ln -s ../publis .
