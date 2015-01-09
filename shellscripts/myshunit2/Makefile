shunit2_version = 2.1.6
shunit2_tarball_url = https://shunit2.googlecode.com/files/shunit2-$(shunit2_version).tgz

shunit2_tarball_path = ./test/lib/shunit2-$(shunit2_version).tgz
shunit2_path = $(shunit2_tarball_path:%.tgz=%)
shunit2_main_path = $(shunit2_path)/src/shunit2

test_targets = $(wildcard test/*.sh)
test_run_targets = $(test_targets:test/%.sh=%.run)

default: all

test: $(test_run_targets)

.PHONY: default all test $(test_run_targets)

$(test_run_targets): %.run: test/%.sh $(shunit2_path)
	SHUNIT2_MAIN_PATH=$(shunit2_main_path) sh $<

$(shunit2_path): $(shunit2_tarball_path)
	tar -xf $< -C `dirname $@`
	touch $@

$(shunit2_tarball_path):
	mkdir -p `dirname $@`
	wget -O $@ $(shunit2_tarball_url)
