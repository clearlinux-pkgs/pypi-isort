#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-isort
Version  : 5.11.0
Release  : 112
URL      : https://files.pythonhosted.org/packages/ee/00/c5929aab9d7459d2b32dbbd2a013f591503f3f0a5e346226aa1ceb7f7989/isort-5.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ee/00/c5929aab9d7459d2b32dbbd2a013f591503f3f0a5e346226aa1ceb7f7989/isort-5.11.0.tar.gz
Summary  : A Python utility / library to sort Python imports.
Group    : Development/Tools
License  : MIT
Requires: pypi-isort-bin = %{version}-%{release}
Requires: pypi-isort-license = %{version}-%{release}
Requires: pypi-isort-python = %{version}-%{release}
Requires: pypi-isort-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
[![isort - isort your imports, so you don't have to.](https://raw.githubusercontent.com/pycqa/isort/main/art/logo_large.png)](https://pycqa.github.io/isort/)

%package bin
Summary: bin components for the pypi-isort package.
Group: Binaries
Requires: pypi-isort-license = %{version}-%{release}

%description bin
bin components for the pypi-isort package.


%package license
Summary: license components for the pypi-isort package.
Group: Default

%description license
license components for the pypi-isort package.


%package python
Summary: python components for the pypi-isort package.
Group: Default
Requires: pypi-isort-python3 = %{version}-%{release}

%description python
python components for the pypi-isort package.


%package python3
Summary: python3 components for the pypi-isort package.
Group: Default
Requires: python3-core
Provides: pypi(isort)

%description python3
python3 components for the pypi-isort package.


%prep
%setup -q -n isort-5.11.0
cd %{_builddir}/isort-5.11.0
pushd ..
cp -a isort-5.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670882707
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-isort
cp %{_builddir}/isort-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-isort/00afc6bf25b2c1776f00c130bbf4397210ce7766 || :
cp %{_builddir}/isort-%{version}/isort/_vendored/tomli/LICENSE %{buildroot}/usr/share/package-licenses/pypi-isort/9da6ca26337a886fb3e8d30efd4aeda623dc9ade || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## install_append content
rm -rf %{buildroot}/usr/lib/python3*/site-packages/tests
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isort
/usr/bin/isort-identify-imports

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-isort/00afc6bf25b2c1776f00c130bbf4397210ce7766
/usr/share/package-licenses/pypi-isort/9da6ca26337a886fb3e8d30efd4aeda623dc9ade

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
