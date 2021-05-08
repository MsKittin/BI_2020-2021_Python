import os
import shutil
import tempfile
import unittest
import fastq_filtrator as filtering


class ConfigTest(unittest.TestCase):

    def setUp(self) -> None:
        self.fastq_file_path = 'example.fastq'

    def test_raises_error_if_min_length_is_not_integer(self):
        arguments = ['--min_length', 'a']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(TypeError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_min_length_not_greater_than_0(self):
        arguments = ['--min_length', '0']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(ValueError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_min_length_values_empty(self):
        arguments = ['--min_length']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(ValueError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_lower_gc_bound_is_less_than_0(self):
        arguments = ['--gc_bounds', '-1', '30']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(ValueError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_lower_bound_is_greater_than_upper(self):
        arguments = ['--gc_bounds', '40', '30']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(ValueError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_lower_bound_is_not_integer(self):
        arguments = ['--gc_bounds', 'a', '30']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(TypeError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_upper_bound_is_not_integer(self):
        arguments = ['--gc_bounds', '30', 'a']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(TypeError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_upper_gc_bound_is_less_than_0(self):
        arguments = ['--gc_bounds', '30', '-1']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(ValueError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_gc_bounds_values_empty(self):
        arguments = ['--gc_bounds']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(ValueError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_if_output_base_name_value_empty(self):
        arguments = ['--output_base_name']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(ValueError):
            filtering.init_config(config, arguments=arguments)

    def test_raises_error_unexpected_argument(self):
        arguments = ['--some_argument']
        config = filtering.Config(self.fastq_file_path)

        with self.assertRaises(NameError):
            filtering.init_config(config, arguments=arguments)


class SecondaryFunctionsTest(unittest.TestCase):

    def test_gc_percent(self):
        read = 'ATGC'
        result = filtering.GC_percent(read)
        self.assertEqual(result, 50)

    def test_gc_bounds(self):
        seq = 'ATGC'
        self.assertTrue(filtering.GC_bounds(seq, lower_bound=30, upper_bound=70))
        self.assertFalse(filtering.GC_bounds(seq, lower_bound=60, upper_bound=70))

    def test_min_len_find(self):
        seq = 'ATGC'
        self.assertTrue(filtering.min_len_find(seq, minlen=3))
        self.assertFalse(filtering.min_len_find(seq, minlen=7))


class FiltratorOutputTest(unittest.TestCase):

    def setUp(self):
        self.original_working_dir = os.getcwd()
        self.test_dir = tempfile.mkdtemp()

        self.fastq_file_path = 'example.fastq'
        temp_dir_fastq_file_path = os.path.join(self.test_dir, self.fastq_file_path)
        shutil.copyfile(self.fastq_file_path, temp_dir_fastq_file_path)

        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self.original_working_dir)
        shutil.rmtree(self.test_dir)

    def test_output_file_without_extension(self):
        arguments = ['--min_length', '55', self.fastq_file_path]
        filtering.main(arguments)

        self.assertTrue(os.path.exists("example"))

    def test_output_base_name_output_naming(self):
        arguments = ['--min_length', '55', '--output_base_name', 'somename', self.fastq_file_path]
        filtering.main(arguments)

        self.assertTrue(os.path.exists("somename"))

    def test_keep_filtered_output_naming(self):
        arguments = ['--min_length', '55', '--output_base_name', 'somename', '--keep_filtered', self.fastq_file_path]
        filtering.main(arguments)

        self.assertTrue(os.path.exists("somename__passed.fastq"))
        self.assertTrue(os.path.exists("somename__failed.fastq"))


if __name__ == '__main__':
    unittest.main()
