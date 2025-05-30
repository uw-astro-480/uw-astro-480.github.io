# Frequently Asked Questions

## Pushing commits to GitHub prompts for a username and password

This most likely happens because you cloned the repository using the HTTPS version of the repo URL. This will allow you to clone but GitHub does not longer allow password authentication for pushing commits. When cloning always make sure you use the SSH version which should look like `git@github.com:uw-astro-480/...`

```{figure} ./images/clone-ssh.png
:width: 80%
:align: center
```

If you have already cloned the repository using HTTPS, you can change the remote URL to use SSH by running, from the root of the repository:

```bash
git remote set-url origin git@github.com:uw-astro-480/...
```

(replace the `...` with the actual path to your repository). You can check that the remote URL has been changed by running:

```bash
git remote -vvv
```

## The local/remote tests keep failing

If the automatic tests are failing make sure that you look at the error message. In GitHub you can do that by navigating to the repository, clicking on `Actions`, selecting the last workflow run, clicking on `Autograding` and then in `Test with pytest`.

Remember that the tests are pretty dump. What they do is to import certain functions and call them with some test data and check that the returned value makes some sense. _If you change the signature of the function the test won't work_. For example imaging that you are asked to implement a function that returns the sum of two numbers:

```python
def add(a, b):
    return a + b
```

If you change the signature to:

```python
def add(a, b, c):
    return a + b + c
```

The test will fail because when it calls `add(1, 2)` the function call will raise an error.
