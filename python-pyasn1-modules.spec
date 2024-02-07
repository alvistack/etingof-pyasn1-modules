# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pyasn1-modules
Epoch: 100
Version: 0.4.0
Release: 1%{?dist}
BuildArch: noarch
Summary: ASN.1 modules for pyasn1 library
License: BSD-3-Clause
URL: https://github.com/pyasn1/pyasn1-modules/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The pyasn1-modules package contains a collection of ASN.1 data
structures expressed as Python classes based on pyasn1 data model.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pyasn1-modules
Summary: ASN.1 modules for pyasn1 library
Requires: python3
Requires: python3-pyasn1 >= 0.4.6
Provides: python3-pyasn1-modules = %{epoch}:%{version}-%{release}
Provides: python3dist(pyasn1-modules) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyasn1-modules = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyasn1-modules) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyasn1-modules = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyasn1-modules) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pyasn1-modules
The pyasn1-modules package contains a collection of ASN.1 data
structures expressed as Python classes based on pyasn1 data model.

%files -n python%{python3_version_nodots}-pyasn1-modules
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pyasn1-modules
Summary: ASN.1 modules for pyasn1 library
Requires: python3
Requires: python3-pyasn1 >= 0.4.6
Provides: python3-pyasn1-modules = %{epoch}:%{version}-%{release}
Provides: python3dist(pyasn1-modules) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyasn1-modules = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyasn1-modules) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyasn1-modules = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyasn1-modules) = %{epoch}:%{version}-%{release}

%description -n python3-pyasn1-modules
The pyasn1-modules package contains a collection of ASN.1 data
structures expressed as Python classes based on pyasn1 data model.

%files -n python3-pyasn1-modules
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
