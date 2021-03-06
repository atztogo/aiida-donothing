"""AiiDA calculation provided by aiida_donothing."""
from aiida.orm import Int
from aiida.engine import CalcJob
from aiida.common import CalcInfo, CodeInfo


class DoNothingCalculation(CalcJob):
    """AiiDA calculation plugin for doing nothing."""

    @classmethod
    def define(cls, spec):
        """Define inputs and outputs of the calculation."""
        super().define(spec)
        spec.input(
            "metadata.options.resources",
            valid_type=dict,
            default={"num_machines": 1, "num_mpiprocs_per_machine": 1},
        )
        spec.input("metadata.options.parser_name", default="donothing.donothing")
        # spec.input(
        #     "metadata.options.output_filename",
        #     valid_type=str,
        #     default="donothing.log",
        # )
        spec.input("metadata.options.withmpi", valid_type=bool, default=False)
        spec.input(
            "seconds",
            valid_type=Int,
            default=lambda: Int(60 * 60 * 10),
            help="Seconds to sleep.",
        )
        # spec.exit_code(
        #     300,
        #     "ERROR_MISSING_OUTPUT_FILES",
        #     message="Calculation did not produce all expected output files.",
        # )

    def prepare_for_submission(self, folder):
        """Create input files.

        stdout_name is optional. Wihtout it, no output file is generated.

        """
        codeinfo = CodeInfo()
        codeinfo.cmdline_params = [f"{self.inputs.seconds.value}"]
        codeinfo.code_uuid = self.inputs.code.uuid
        # codeinfo.stdout_name = self.metadata.options.output_filename
        codeinfo.withmpi = self.inputs.metadata.options.withmpi

        # Prepare a `CalcInfo` to be returned to the engine
        calcinfo = CalcInfo()
        calcinfo.codes_info = [codeinfo]
        calcinfo.local_copy_list = []
        calcinfo.retrieve_list = []
        # calcinfo.retrieve_list = [self.metadata.options.output_filename]

        return calcinfo
