.PHONY: create-practice remove-practice

create-practice:
ifdef NAME
	$(error NAME is not defined)
endif
	mkdir -p $(NAME)
	cp PracticeMakefile $(NAME)/Makefile

remove-practice:
ifdef NAME
	$(error NAME is not defined)
endif
	rm -rf $(NAME)



