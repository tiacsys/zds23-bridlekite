@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXTAGS%" == "" (
	set SPHINXTAGS=-t nx
)
if "%SPHINXOPTS%" == "" (
	set SPHINXOPTS=-v -W --keep-going
)
if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

if "%DECKTAPEBUILD%" == "" (
	set DECKTAPEBUILD=%CD%/%BUILDDIR%/revealjs/decktape-build
)

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help
if "%1" == "revealjspdf" goto revealjspdf

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% -t %1 %SPHINXTAGS% %SPHINXOPTS% %O%
goto end

:revealjspdf
%DECKTAPEBUILD%
if errorlevel 9009 (
	echo.
	echo.The 'decktape-build' command was not found. Make sure you have
	echo.DeckTape installed and revealjs was always build, then set the
	echo.DECKTAPEBUILD environment variable to point to the full path of
	echo.the 'decktape' executable. Alternatively you may add the DeckTape
	echo.directory to PATH.
	exit /b 1
)
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
echo.
echo.Add-ons:
echo.  revealjs    to make Reveal.js standalone HTML presentation (if enabled)
echo.  revealjspdf to make PDF export from Reveal.js presentation (if enabled)
echo.  spelling    to check spelling in the documentation (if enabled)

:end
popd
