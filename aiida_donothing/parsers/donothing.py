"""Parsers provided by aiida_donothing."""
from aiida.engine import ExitCode
from aiida.parsers.parser import Parser
from aiida.common import exceptions

from aiida_donothing.calculations.donothing import DoNothingCalculation


class DoNothingParser(Parser):
    """AiiDA parser plugin for doing nothing."""

    def __init__(self, node):
        """Init method."""
        super().__init__(node)
        if not issubclass(node.process_class, DoNothingCalculation):
            raise exceptions.ParsingError("Can only parse DoNothingCalculation")

    def parse(self, **kwargs):
        """Parse outputs, store results in database.

        Do nothing although we can do something like below.

        output_filename = self.node.get_option("output_filename")
        filenames_retrieved = self.retrieved.list_object_names()
        if output_filename not in filenames_retrieved:
            return self.exit_codes.ERROR_MISSING_OUTPUT_FILES
        for filename in filenames_retrieved:
            self.logger.info("Parsing '{}'".format(filename))
            with self.retrieved.open(filename, "rb") as handle:
                output_node = SinglefileData(file=handle)
                self.out(filename, output_node)

        """
        return ExitCode(0)
