# This shell script is required by the doc-builder. Moving it might break
# the doc-building pipeline
if [[ $(arch) == 'arm64' ]]; then
      brew install pandoc
else
    sudo apt-get update
    sudo apt-get install pandoc -y
fi