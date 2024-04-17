LIBRARY_DIR ?= ../..
OUTPUT_BASE_DIR ?= ..

help: common-help

include $(LIBRARY_DIR)/ubinos/make/common.mk
-include $(LIBRARY_DIR)/ubinos/make/custom.mk

%: common-% ;

all config configd build clean cleand rebuild rebuildd dserver xdserver load reset run xrun debug xdebug attach xattach xconfig menuconfig doc cleandoc xopendoc env cleanenv test:
	make -C $(LIBRARY_DIR)/sphinx_doc_materials/make -f makefile.mk         OUTPUT_BASE_DIR=$(realpath $(OUTPUT_BASE_DIR)) LIBRARY_DIR=$(realpath $(LIBRARY_DIR)) CONFIG_DIR=$(realpath $(CONFIG_DIR)) CONFIG_NAME=$(CONFIG_NAME) DEBUG_SERVER_SERIAL=$(DEBUG_SERVER_SERIAL) DEBUG_SERVER_PORT=$(DEBUG_SERVER_PORT) $@
