add_rules("mode.debug", "mode.release")


target("硬件部_王浩霖")
    set_kind("binary")
    add_files("src/*.cpp")
    add_includedirs("include")
    add_packages("nlohmann_json", "cpp-httplib")
