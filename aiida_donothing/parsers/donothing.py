"""Parsers provided by aiida_donothing."""
from aiida.engine import ExitCode
from aiida.parsers.parser import Parser
from aiida.common import exceptions
from aiida.orm import SinglefileData

from aiida_donothing.calculations.donothing import DoNothingCalculation


class DoNothingParser(Parser):
    """AiiDA parser plugin for doing nothing."""

    def __init__(self, node):
        """Init method."""
        super().__init__(node)
        if not issubclass(node.process_class, DoNothingCalculation):
            raise exceptions.ParsingError("Can only parse DoNothingCalculation")

    def parse(self, **kwargs):
        """Parse outputs, store results in database."""
        output_filename = self.node.get_option("output_filename")

        # Check that folder content is as expected
        if False:
            return self.exit_codes.ERROR_MISSING_OUTPUT_FILES

        # add output file
        self.logger.info("Parsing '{}'".format(output_filename))
        with self.retrieved.open(output_filename, "rb") as handle:
            output_node = SinglefileData(file=handle)
        self.out("diff", output_node)

        return ExitCode(0)
