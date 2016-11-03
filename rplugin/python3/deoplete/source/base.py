# ============================================================================
# FILE: base.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import re
from abc import abstractmethod
from deoplete.logger import LoggingMixin


class Base(LoggingMixin):

    def __init__(self, vim):
        self.vim = vim
        self.description = ''
        self.mark = ''
        self.max_pattern_length = 80
        self.input_pattern = ''
        self.matchers = [
            'matcher_length', 'matcher_fuzzy']
        self.sorters = ['sorter_rank']
        self.converters = [
            'converter_remove_overlap',
            'converter_truncate_abbr',
            'converter_truncate_menu']
        self.filetypes = []
        self.is_bytepos = False
        self.is_initialized = False
        self.rank = 100
        self.disabled_syntaxes = []

    def get_complete_position(self, context):
        if self.input_pattern:
            pattern = self.input_pattern
        else:
            pattern = context['keyword_patterns']
        m = re.search('(?:' + pattern + ')$', context['input'])
        return m.start() if m else -1

    @abstractmethod
    def gather_candidate(self, context):
        pass

    def on_event(self, context):
        pass
