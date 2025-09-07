# Customized OpenCompass API

This repository provides an example of how to use a customized API model within OpenCompass. (This readme is provided by ChatGPT4o-mini.)

## Setup Instructions

1. **Configure API Settings**
    Set your `API_BASE` and `KEY` in the following files:

   - `my_api.py`
   - `./mymode/default.py`

2. **Integrate Your API Model**

   - Copy `my_api.py` to `<your_package_path>/opencompass/models`.

   - Add the following import statement to `<your_package_path>/opencompass/models/__init__.py`

     ```python
     from .my_api import MyModelAPI
     ```

3. **Copy Configuration Files**
    Copy the `./mymode` directory to `<your_package_path>/opencompass/configs/models`.

4. **Run Your Process**
    Execute your process with a command like:

   ```shell
   opencompass example_gsm8k.py
   ```

## References

- [OpenCompass GitHub Repository](https://github.com/open-compass/opencompass): OpenCompass is an LLM evaluation platform supporting a wide range of models (Llama3, Mistral, InternLM2, GPT-4, LLaMa2, Qwen, GLM, Claude, etc.) across 100+ datasets.
- [OpenCompass Documentation](https://opencompass.readthedocs.io/en/latest/): Comprehensive documentation for OpenCompass 0.5.0.

Feel free to reach out for any questions or contributions!5.0 documentation](https://opencompass.readthedocs.io/en/latest/)