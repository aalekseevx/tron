# from sandbox_config import SANDBOX_PROFILE_PATH, SANDBOX
import subprocess as sp

class Sandbox:
    @staticmethod
    def generate_profile():
        pass
        # profile = open(SANDBOX_PROFILE_PATH, "w")
        # for option in SANDBOX["options"]:
        #     profile.write("{0}\n".format(option))
        # for bl_dir in SANDBOX["blacklisted_dirs"]:
        #     profile.write("blacklist {0}\n".format(bl_dir))
        # for rlimits in SANDBOX["rlimits"]:
        #     profile.write("{0}\n".format(rlimits))

    @staticmethod
    def run(command, executable_filename):
        print(command)
        print(os.pwd())
        return sp.Popen(command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
        # return sp.Popen(SANDBOX["command"] + [f"--private={executable_filename}"] + command, stdin=sp.PIPE, stdout=sp.PIPE,
                        # stderr=sp.PIPE, universal_newlines=True)
